import cv2
import face_recognition
import playsound
import threading

cap = cv2.VideoCapture(0)
sound_played = False

def ring_bell():
    playsound.playsound('doorbell_sound.mp3')

while True:
    _, frame = cap.read()

    faces = face_recognition.face_locations(frame)

    if faces and not sound_played:
        threading.Thread(target=ring_bell).start()
        # Play the sound in a separate thread to avoid blocking the main thread
        # This allows the sound to play while the program continues to run
        sound_played = True

    elif not faces and sound_played:
        sound_played = False

    cv2.imshow('Smart Doorbell by Python_Programmer.12', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        # If you want to stop the sound, you can implement a method to stop the sound here
        # For example, you can use a flag or a signal to stop the sound thread
        # However, this may require additional libraries or methods to stop the sound
        # For simplicity, we will just exit the program here
        # and the sound will stop playing when the program exits
        # You can also use a library like pyaudio to control the sound playback
        # or implement a more complex sound management system if needed
        # For now, we will just exit the program and let the sound finish playing
        # before the program exits
        # This is a simple implementation and may not be suitable for all use cases
        # You can modify the code to suit your needs and requirements
        # For example, you can add a button to stop the sound or implement a more complex sound management system
        # if needed
        # For now, we will just exit the program and let the sound finish playing
        # before the program exits
        exit(0)
        # This is a simple implementation and may not be suitable for all use cases
        break