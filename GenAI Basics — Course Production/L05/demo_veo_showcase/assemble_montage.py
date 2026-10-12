import os
import sys
import subprocess
import pathlib

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def assemble():
    folder = pathlib.Path(__file__).parent
    s1 = folder / 'shot1.mp4'
    s2 = folder / 'shot2.mp4'
    s3 = folder / 'shot3.mp4'
    out = folder / 'courier_delivery_final.mp4'

    if not (s1.exists() and s2.exists() and s3.exists()):
        print('[ERROR] Missing shot1.mp4, shot2.mp4 or shot3.mp4!')
        return

    # High compatibility settings: yuv420p + faststart + audio acrossfade
    cmd = [
        'ffmpeg', '-y',
        '-i', str(s1),
        '-i', str(s2),
        '-i', str(s3),
        '-filter_complex',
        '[0:v][1:v]xfade=transition=wipeleft:duration=0.5:offset=7.5[v1]; '
        '[v1][2:v]xfade=transition=fadeblack:duration=0.5:offset=15.0[outv]; '
        '[0:a][1:a]acrossfade=d=0.5[a1]; '
        '[a1][2:a]acrossfade=d=0.5[outa]',
        '-map', '[outv]',
        '-map', '[outa]',
        '-c:v', 'libx264',
        '-pix_fmt', 'yuv420p',
        '-profile:v', 'high',
        '-level', '4.1',
        '-c:a', 'aac',
        '-b:a', '192k',
        '-movflags', '+faststart',
        str(out)
    ]
    print('[FFMPEG] Assembling shots with transitions and universal Windows compatibility...')
    res = subprocess.run(cmd)
    if res.returncode == 0:
        print(f'[SUCCESS] Rendered final montage: {out}')
    else:
        print(f'[FAIL] FFmpeg exited with code: {res.returncode}')

if __name__ == '__main__':
    assemble()
