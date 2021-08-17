import json
import os

from glob2 import glob

from trclab.utils.ProgressBar import ProgressBar
from trclab.vhp.OrganImage import OrganImage
from trclab.vhp.OrganImageReader import OrganImageReader


class OrganDataset:
    def __init__(self, image_dir: str, extension: str = "*.jpg"):
        self.images = list()
        self.extension = extension
        self.images_label = None

        load_images = glob(os.path.join(image_dir, extension), recursive=True)
        progress_bar = ProgressBar(len(load_images), title="Loaded Organ Dataset")
        for img in load_images:
            progress_bar.update("process image %s" % os.path.basename(img))
            self.images.append(OrganImage(img))

        progress_bar.finish('Dataset loaded successful!')

    def set_label(self, vhp_label):
        self.images_label = vhp_label

    def export_label_area(self, target_dir, patten: str, output_file):
        if self.images_label is None:
            raise FileNotFoundError

        progress_bar = ProgressBar(len(self.images), "Export label area")
        counter = 0

        export_file = open(output_file, 'w')
        export_file.write("{\n}")
        export_file.close()
        export_file = open(output_file, 'r')
        export_data = export_file.read()
        data = json.loads(export_data)

        target_name_split = patten.split('.')
        target_extension = target_name_split[len(target_name_split) - 1]

        for image in self.images:
            counter += 1
            progress_bar.update("Process Image (%s/%s)" % (counter, len(self.images)))
            oir = OrganImageReader(image, self.images_label, progress_bar)
            progress_bar.update("Find organ and get list (%s/%s)" % (counter, len(self.images)), just_message=True)
            organ_list = oir.find_organ()
            progress_bar.update("Get index of all founded organs (%s/%s)" % (counter, len(self.images)),
                                just_message=True)

            target_basename = image.basename[:-len(image.extension)] + target_extension
            target_file_size = os.path.getsize(os.path.join(target_dir, target_basename))
            key = target_basename + str(target_file_size)

            data[key] = {}
            data[key]['fileref'] = ''
            data[key]['size'] = target_file_size
            data[key]['filename'] = target_basename
            data[key]['base64_img_data'] = ''
            data[key]['file_attributes'] = {}
            data[key]['regions'] = {}

            region_idx = 0
            progress_bar.update("Start Process %s (%s/%s)" % (key, counter, len(self.images)), just_message=True)
            for organ in organ_list:
                index = oir.get_index(organ)
                filter_image = oir.filter_from_index(index)
                contours = oir.get_contours(filter_image)
                for n in range(0, len(contours)):
                    progress_bar.update("Processing... %s-%d (%s/%s)" % (key, n, counter, len(self.images)),
                                        just_message=True)
                    list_x = []
                    list_y = []
                    for point in contours[n]:
                        for x, y in point:
                            list_x.append(x)
                            list_y.append(y)

                    data[key]['regions'][region_idx] = {}
                    data[key]['regions'][region_idx]['shape_attributes'] = {}
                    data[key]['regions'][region_idx]['shape_attributes']['name'] = 'polygon'
                    data[key]['regions'][region_idx]['shape_attributes']['all_points_x'] = list_x
                    data[key]['regions'][region_idx]['shape_attributes']['all_points_y'] = list_y
                    data[key]['regions'][region_idx]['region_attributes'] = {}
                    data[key]['regions'][region_idx]['region_attributes']['name'] = str(oir.get_index(organ))
                    region_idx += 1
                progress_bar.update("%s Process successful! (%s/%s)" % (key, counter, len(self.images)),
                                    just_message=True)

        progress_bar.finish("Exported label area successful!")
        with open(output_file, 'w') as out_file:
            json.dump(data, out_file, default=int)
