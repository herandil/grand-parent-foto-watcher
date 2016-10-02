from django.core.files.storage import FileSystemStorage
from base.functions import randomHash
from database.models import Photos, User
import PIL
from PIL import Image


class ImageUploader:

    def __init__(self, image, user_id):
        self.image = image
        self.name = image.name
        self.size = image.size
        self.content_type = image.content_type
        self.user_id = user_id

        self.image_path = 'media'
        self.image_thumbnail_path = 'media/thumbnail'
        self.max_size = 4 * 1024 * 1024  # 4MB
        self.mime_list = ['image/png', 'image/jpeg', 'image/gif']
        self.extension_list = ['png', 'jpeg', 'jpg', 'gif']
        self.dir_path = '/www/website/media/'
        self.dir_path_thumbnail = '/www/website/media/thumbnail/'

    def check_mime_image(self):
        for mime in self.mime_list:
            if self.content_type == mime:
                return True

        return False

    def check_extension(self):
        string_array = self.name.split('.')
        amount = len(string_array)
        extension = string_array[amount - 1]
        for ext in self.extension_list:
            if extension == ext:
                return True

        return False

    def image_name_builder(self):
        string_array = self.name.split('.')
        amount = len(string_array)
        extension = string_array[amount - 1]

        title = randomHash.RandomHash.generate()
        new_name = title + '.' + extension
        return new_name

    def make_thumbnail(self, image_name):
        base_width = 150
        img = Image.open(self.dir_path + image_name)
        # calculate
        wpercent = (base_width / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        # resize image
        img = img.resize((base_width, hsize), PIL.Image.ANTIALIAS)
        img.save(self.dir_path_thumbnail + image_name)

    def image_uploader(self, dirname, name):
        fs = FileSystemStorage(dirname)
        fs.save(name, self.image)

    def save_to_database(self, new_name):
        user = User.objects.get(id=self.user_id)
        photo = Photos()
        photo.title = self.name
        photo.desc = "bla bla"
        photo.src = new_name
        photo.size = self.size
        photo.user = user
        photo.save()

    def check_user_can_upload(self):
        return 'test'

    def upload(self):
        print 'uploading...'
        if self.check_extension():
            print 'Checked extension!'
            if self.check_mime_image():
                if self.size < self.max_size:
                    # TODO check if user is able to upload more.
                    # TODO put user id with uploaded photo.
                    # TODO make photo pages.
                    new_name = self.image_name_builder()

                    # self.image_uploader('media/thumbnail', new_name)
                    self.image_uploader('media', new_name)
                    self.make_thumbnail(new_name)
                    self.save_to_database(new_name)
                    return True
        return False






