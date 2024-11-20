import cv2
import os
from deepface import DeepFace as df
import threading
from pathlib import Path
# Disable TensorFlow's oneDNN optimizations
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

class FacialRecognition:
    def __init__(self):
        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 500)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 500)
        self.counter = 0
        self.face_match = False
        self.base_dir= Path(__file__).parent #Finds the script directory
        self.image_path = self.base_dir / "known_faces" / "Aditya.jpg"
        self.reference_img = cv2.imread(str(self.image_path))
        if self.reference_img is None:
            raise FileNotFoundError("Reference image could not be loaded. Check the file path.")

    def Face_check(self, frame):
        #Verifies the captured frame against the reference image using DeepFace.
        try:
            if frame is None:
                raise ValueError("Invalid frame provided!")
            
            # Perform DeepFace verification
            result = df.verify(frame, self.reference_img)

            if isinstance(result, dict):  # If the result is a dictionary
                self.face_match = result.get("verified", False)
            elif isinstance(result, bool):  # If the result is a boolean (direct match/no match)
                self.face_match = result
            else:
                print(f"Unexpected result from DeepFace.verify: {result}")
                self.face_match = False
        except Exception as e:
            print(f"Error in Face_check: {e}")
            self.face_match = False

    def main(self):
        #Main loop for capturing video and performing facial recognition.
        while True:
            ret, frame = self.cap.read()
            if ret:
                # Process frame every 90 frames (adjust as needed)
                if self.counter % 90 == 0:
                    try:
                        threading.Thread(target=self.Face_check, args=(frame.copy(),)).start()
                    except Exception as e:
                        print(f"Error starting thread: {e}")
                self.counter += 1

                # Display result based on face_match status
                if self.face_match:
                    cv2.putText(frame, "MATCH!", (20, 450), cv2.FONT_ITALIC, 2, (0, 255, 0), 2)
                else:
                    cv2.putText(frame, "NO MATCH!", (20, 450), cv2.FONT_ITALIC, 2, (0, 0, 255), 2)

                cv2.imshow("video", frame)

            # Exit loop on pressing 'q'
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        self.cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    try:
        FacialRecognition().main()
    except Exception as e:
        print(f"Application Error: {e}")