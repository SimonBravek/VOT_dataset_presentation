import cv2
import os

vot_path = "C:/Users/wbras/9 DataSet/vot23-init-dataset-ext/"
video_name = "my_video.mp4"

list_vot_child = os.listdir(vot_path)

#creates loop for each child
for child in list_vot_child:
   vot_child_path = vot_path + child + "/"
   color_path = vot_child_path + "color/"
   list_img_nums = os.listdir(color_path)

   #creates a list of img paths for each child
   list_num_paths = []
   for num in list_img_nums: 
      num_path = color_path + num
      list_num_paths.append(num_path)
   #here exists list_num_paths that contains all the imgs in every child loop

   video_full_path = vot_child_path + video_name
   cv2_fourcc = cv2.VideoWriter_fourcc(*'mp4v')
   frame = cv2.imread(list_num_paths[0])
   size = list(frame.shape) #creates list out of touples or every symbol
   del size[2]
   size.reverse() #make reverse order
   video_property = cv2.VideoWriter(video_full_path, cv2_fourcc, 30, size) #output video full path, fourcc, fps, size

   for i in range(len(list_num_paths)): 
      video_property.write(cv2.imread(list_num_paths[i]))
      print('frame ', i+1, ' of ', len(list_num_paths))

   video_property.release()
   video_number = list_vot_child.index(child) + 1
   print('Outputed video number ', str(video_number), 'to ', video_full_path)

print('Done successfully!')