import cv2
import time

print("🔍 Checking OpenCV version...")
print("OpenCV version:", cv2.__version__)

# Try multiple camera indexes if needed
for cam_index in range(2):
    print(f"🔌 Trying camera index {cam_index}...")
    cap = cv2.VideoCapture(cam_index)

    if cap.isOpened():
        print(f"✅ Camera {cam_index} opened successfully!")
        break
    else:
        print(f"❌ Camera {cam_index} failed.")
        cap.release()
        cap = None

if not cap or not cap.isOpened():
    print("🚫 No working camera found. Exiting.")
    exit()

print("📷 Live feed starting... Press 'q' to quit.")

while True:
    ret, frame = cap.read()

    if not ret:
        print("❌ Frame not read correctly. Retrying...")
        time.sleep(0.5)
        continue

    cv2.imshow("Camera Test", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("👋 Quitting.")
        break

cap.release()
cv2.destroyAllWindows()
