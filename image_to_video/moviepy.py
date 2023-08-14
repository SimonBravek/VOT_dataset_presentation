
import cv2
import os

def create_compressed_video(color_path, output_folder, frame_rate, fourcc, video_name):
    list_img_nums = os.listdir(color_path)

    video_full_path = os.path.join(output_folder, video_name)
    list_num_paths = [os.path.join(color_path, num) for num in list_img_nums]

    frame = cv2.imread(list_num_paths[0])
    size = (int(frame.shape[1]), int(frame.shape[0]))  # Calculate the new size after resizing

    # Define the codec and create VideoWriter object using H.265 (HEVC) codec
    cv2_fourcc = cv2.VideoWriter_fourcc(*fourcc)
    video_property = cv2.VideoWriter(video_full_path, cv2_fourcc, frame_rate, size)  # Create the VideoWriter object
    for img in list_num_paths:
        image = cv2.imread(img)  # Read the image using cv2.imread
        compressed_image = cv2.resize(image, size)  # Resize the image
        video_property.write(compressed_image)  # Write the resized frame to the video
        round = str(list_num_paths.index(img) + 1)
        total = str(len(list_num_paths))
        print('Image number ' + round + ' of total ' + total + ' just completed!')

    print('Before release')
    video_property.release()
    print('After release')


if __name__ == '__main__':
    color_path = "C:/Users/wbras/9 DataSet/vot23-init-dataset-ext/agility/color"
    output_folder = "C:/Users/wbras/9 DataSet/VOT_videa"
    fourcc = 'H264'  # or 'HEVC'
    frame_rate = 30
    video_name = '2.mp4'
    create_compressed_video(color_path, output_folder, frame_rate, fourcc, video_name)