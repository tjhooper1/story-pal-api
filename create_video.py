from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips

def create_video(image_paths, audio_path):
    try:
        audio_clip = AudioFileClip(audio_path)
        duration_per_image = audio_clip.duration / len(image_paths)
        image_clips = []

        for image_path in image_paths:
            clip = ImageClip(image_path).set_duration(duration_per_image)
            image_clips.append(clip)

        video_clip = concatenate_videoclips(image_clips, method="compose")
        video_clip = video_clip.set_audio(audio_clip)
        output_path = 'story.mp4'
        video_clip.write_videofile(output_path, fps=24)
        return output_path
    except Exception as e:
        raise Exception(f"Error creating video: {e}")
