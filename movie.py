import ffmpeg

def concatenate_ffmpeg(video_clip_paths, output_path):
    clips = [ffmpeg.input(c).filter("pad", width="max(iw,ih*(16/9))", height="ow/(16/9)", x="(ow-iw)/2", y="(oh-ih)/2").filter("scale", 1280, 720).filter("setsar", 1, 1) for c in video_clip_paths]
    final_clip = ffmpeg.concat(*clips)
    final_clip.overlay(ffmpeg.input("watermark.png")['v'].filter('scale', "iw-200", -1, force_original_aspect_ratio="decrease"), x="(main_w-overlay_w)", y="(main_h-overlay_h)/(main_h-overlay_h)")
    final_clip.output(output_path).overwrite_output().run()