from pathlib import Path


# class representing a Custom Label JSON line for an image
class cl_json_line:

    def __init__(self, job, img, img_path):

        #Get image info. Annotations are dealt with seperately
        sizes = []
        image_size = {}
        image_size["width"] = img["width"]
        image_size["depth"] = 3
        image_size["height"] = img["height"]
        sizes.append(image_size)

        bounding_box = {}
        bounding_box["annotations"] = []
        bounding_box["image_size"] = sizes

        self.__dict__["source-ref"] = s3_path + img_path + img['file_name']
        self.__dict__[job] = bounding_box

        #get metadata
        metadata = {}
        metadata['job-name'] = job_name
        metadata['class-map'] = {}
        metadata['human-annotated'] = 'yes'
        metadata['objects'] = []
        metadata['creation-date'] = img['file_name']
        metadata['type'] = 'groundtruth/object-detection'

        self.__dict__[job + '-metadata'] = metadata


print("Getting image, annotations, and categories from COCO file...")


def coco_to_manifest(manifest_file, coco_json_file, path_to_img):
    # Create empty manifest file
    open(manifest_file, 'w').close()

    with open(coco_json_file) as f:
        #Get custom label compatible info
        js = json.load(f)
        images = js['images']
        categories = js['categories']
        annotations = js['annotations']

        print('Images: ' + str(len(images)))
        print('annotations: ' + str(len(annotations)))
        print('categories: ' + str(len(categories)))

    print("Creating CL JSON lines...")
    images_dict = {
        image['id']: cl_json_line(label_attribute, image, path_to_img)
        for image in images
    }

    print('Parsing annotations...')
    for annotation in annotations:
        image = images_dict[annotation['image_id']]
        cl_annotation = {}
        cl_class_map = {}

        # get bounding box information
        cl_bounding_box = {}
        cl_bounding_box['left'] = annotation['bbox'][0]
        cl_bounding_box['top'] = annotation['bbox'][1]

        cl_bounding_box['width'] = annotation['bbox'][2]
        cl_bounding_box['height'] = annotation['bbox'][3]
        cl_bounding_box['class_id'] = annotation['category_id']

        getattr(image, label_attribute)['annotations'].append(cl_bounding_box)

        for category in categories:
            if annotation['category_id'] == category['id']:
                getattr(image, label_attribute + '-metadata')['class-map'][
                    category['id']] = category['name']

        cl_object = {}
        cl_object['confidence'] = int(1)  #not currently used by Custom Labels
        getattr(image,
                label_attribute + '-metadata')['objects'].append(cl_object)
    print('Done parsing annotations')

    # Create manifest file.
    print('Writing Custom Labels manifest...')
    for im in images_dict.values():
        with open(manifest_file, 'a+') as outfile:
            json.dump(im.__dict__, outfile)
            outfile.write('\n')
            outfile.close()
