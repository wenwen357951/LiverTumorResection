from trclab.utils.ProgressBar import ProgressBar


class OrganLabel:
    def __init__(self, label_file: str):
        self.labels = []
        self.rgb_list = []
        progress = ProgressBar(sum(1 for _ in open(label_file)), 'Load organ label')
        with open(label_file, 'r') as labels:
            for line in labels:
                line = line.rstrip().replace('\t', ',')
                progress.update("process line '%s'" % line)
                if line.startswith('#') or not line.strip():
                    continue

                rst = line.split(',')
                self.labels.append([rst[0], (int(rst[1]), int(rst[2]), int(rst[3])), rst[4], rst[5]])

            progress.finish("Label loaded successful!")

    def get_rgb_list(self):
        rgb_set = []
        for label in self.labels:
            rgb_set.append(label[1])

        return rgb_set
