import subprocess

def create_video_from_images(image_paths, output_path, fps=30):
    """
    Create a video from a list of image paths using FFmpeg.

    Parameters:
        image_paths (list): List of paths to input images.
        output_path (str): Path to the output video file.
        fps (int): Frames per second for the output video (default is 30).

    Returns:
        None
    """
    ffmpeg_command = [
        "ffmpeg",  # Path to the FFmpeg executable
        "-y",  # Overwrite output files without asking
    ]
    
    # Add individual "-i" options for each image path
    for path in image_paths:
        ffmpeg_command.extend(["-i", path])

    ffmpeg_command.extend([
        "-r", str(fps),  # Set the frame rate of the output video
        "-c:v", "libx264",  # Video codec (H.264)
        "-pix_fmt", "yuv420p",  # Pixel format for compatibility
        output_path  # Output video file path
    ])

    try:
        subprocess.run(ffmpeg_command, check=True)
        print("Video creation successful!")
    except subprocess.CalledProcessError as e:
        print(f"Error creating the video: {e}")
    except FileNotFoundError:
        print("FFmpeg not found. Make sure FFmpeg is installed and accessible in the system's PATH.")

# Example usage:
# (Your image_paths and output_video_path remain the same)
