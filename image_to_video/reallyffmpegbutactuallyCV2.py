import cv2

def compress_video(input_file, output_file, codec, some_compression_factor):
    cap = cv2.VideoCapture(input_file)
    fps = cap.get(cv2.CAP_PROP_FPS)
    width, height = map(int, resolution.split('x'))
    fourcc = cv2.VideoWriter_fourcc(*'X264')  # H.264 codec (libx264)

    # Set output video parameters
    out = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Resize the frame
        frame = cv2.resize(frame, (width, height))

        # Write the frame to the output video
        out.write(frame)

    # Release video objects
    cap.release()
    out.release()

if __name__ == '__main__':
  input_file = 'C:/Users/wbras/Downloads/someone.mp4'
  output_file = 'C:/Users/wbras/Downloads/outppppppppppput.mp4'
  resolution = '1280x720'
  some_compression_factor = 30
  codec = 'h264'

  compressed_video = compress_video(input_file, output_file, codec, some_compression_factor)

  print(f'Compressed video saved to: {compressed_video}')
