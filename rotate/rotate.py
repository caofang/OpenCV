import argparse
import cv2


def run_app(src, dest, degree=0, flip_h=False, flip_v=True):
    cap = cv2.VideoCapture(src)
    
    
    width= int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height= int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps= int(cap.get(cv2.CAP_PROP_FPS))
    size = (height,width)   # 90 deg, swap w, h

    writer= cv2.VideoWriter(dest, cv2.VideoWriter_fourcc(*'DIVX'), fps, size)



    if (cap.isOpened() == False):
        print("Error opening video  file")

    # Read until video is completed
    while(cap.isOpened()):

        ret, frame = cap.read()
        if ret == True:

            image = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)

            cv2.imshow('Frame', image)
            writer.write(image)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', type=int, help='Rotation, Counterclock degree', default=90)
    parser.add_argument('-flip_h', default=0, help='horizatonal flip', action='store_true')
    parser.add_argument('-flip_v', default=0, help='horizatonal flip', action='store_true')
    args = parser.parse_args()

    src = "rotate/session_0.mp4"
    dest = "rotate/output_0.mp4"

    run_app(src, dest, degree=args.d)
    
    
    # extra audio from video
    # ffmpeg -y -i session_0.mp4 output.wav
    
    # merge audio and video
    # ffmpeg -i output_0.mp4 -i output.wav -c:v copy -c:a aac output_av.mp4
    
    

