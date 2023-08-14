import cv2
import os

def create_videos(source_folder, output_folder, frame_rate):
   list_vot_child = os.listdir(source_folder)
   for child in list_vot_child:
      color_path = os.path.join(source_folder, child, "color")
      list_img_nums = os.listdir(color_path)
      video_name = child + ".mp4"
      video_full_path = os.path.join(output_folder, video_name)
      list_num_paths = [os.path.join(color_path, num) for num in list_img_nums]

      for i in range(len(list_num_paths)):
         video_property.write(cv2.imread(list_num_paths[i]))

      cv2_fourcc = cv2.VideoWriter_fourcc(*fourcc)
      frame = cv2.imread(list_num_paths[0])
      size = (frame.shape[1], frame.shape[0])
      video_property = cv2.VideoWriter(video_full_path, cv2_fourcc, frame_rate, size) #output video full path, fourcc, fps, size

      video_property.release()

      video_number = list_vot_child.index(child) + 1
      print('Outputed video number ', str(video_number), 'to ', video_full_path)
   print('Done successfully!')

source_folder = "C:/Users/wbras/9 DataSet/vot23-init-dataset-ext/" #VOT dataset path with structure: MAIN -> SEQUENCES_FOLDERS -> COLOR -> IMGS_BY_NUMBER
output_folder = "C:/Users/wbras/9 DataSet/VOT_videa" # where do u want the result
fourcc = 'mp4v'
frame_rate = 30 #fps, same for all videos

create_videos(source_folder, output_folder, frame_rate)