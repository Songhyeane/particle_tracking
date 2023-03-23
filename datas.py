class data :
    pass

class tiffs(data) :
    def __init__(self,name):
        self.name = name

    def set_cropped_tiffs(self,image,file_path):
        pass

    def set_r_cropped_tiffs(self,image,file_path):
        pass

class paricle(data):
    def __int__(self,name):
        self.name = name

    def set_tracked_particle(self, image, file_path):
        pass

    def set_linear_particle(self, image, file_path):
        pass

    def set_non_linear_particle(self, image, file_path):
        pass


class result(data):
    def __int__(self, name):
        self.name = name

    def set_speed(self, speed, file_path):
        pass

    def set_viscosty(self, speed, file_path):
        pass
