import subprocess, os


def compress_video(input_file, output_file, resolution, some_compression_factor, codec):
  """Compresses a video file.

  Args:
    input_file: The path to the input video file.
    output_file: The path to the output video file.
    resolution: The target resolution of the video.

  Returns:
    The path to the compressed video file.
  """

  command = f'ffmpeg -i {input_file} -c:v {codec} -crf {some_compression_factor} -vf scale={resolution} {output_file}'
  subprocess.run(command, shell=True)

  return output_file

if __name__ == '__main__':
  input_file = 'C:/Users/wbras/Downloads/someone.mp4'
  output_file = 'C:/Users/wbras/Downloads/bbbbbbbbbbb.mp4'
  resolution = '1280x720'
  some_compression_factor = 30
  codec = 'h264'

  compressed_file = compress_video(input_file, output_file, resolution, some_compression_factor, codec)

  print(f'Compressed video saved to: {compressed_file}')