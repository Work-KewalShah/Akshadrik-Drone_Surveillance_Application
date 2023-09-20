import torch
import numpy as np
import cv2
import tkinter as tk
from PIL import Image, ImageTk
import threading

#specifying what to detect depending upon the label provided
def parse_detections(results):
    try:
        detections = results.pandas().xyxy[0]
        detections = detections.to_dict()
        boxes, colors, names, confidence = [], [], [],[]

        for i in range(len(detections["xmin"])):
            confidence = detections["confidence"][i]
            if confidence < 0.2:
                continue
            xmin = int(detections["xmin"][i])
            ymin = int(detections["ymin"][i])
            xmax = int(detections["xmax"][i])
            ymax = int(detections["ymax"][i])
            #print(xmin)
            #print(ymin)
            #print(xmax)
            #print(ymax)
            name = detections["name"][i]
            category = int(detections["class"][i])
            color = COLORS[category]
            if(name == str(detection_source.get()).lower()):
                #confidence.append(confidence)
                boxes.append((xmin, ymin, xmax, ymax))
                colors.append(color)
                names.append(name)
            else:
                pass
            
        return boxes, colors, names
    except Exception as e:
        print(f"1.{e}")

#drawing the detections and label
def draw_detections(boxes, colors, names, img):
    try:
        for box, color, name in zip(boxes, colors, names):
            xmin, ymin, xmax, ymax = box
            cv2.rectangle(
                img,
                (xmin, ymin),
                (xmax, ymax),
                color, 
                2)

            cv2.putText(img, name, (xmin, ymin - 5),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2,
                        lineType=cv2.LINE_AA)
        return img
    except Exception as e:
        print(f"2.{e}")

COLORS = np.random.uniform(0, 255, size=(80, 3))

vid = None

#works when Set Video Source is clicked
def set_vid_source():
    try:
        global vid_source, vid, is_capturing
        vid_source = int(entry_source.get())
        print(f"Video source set to: {vid_source}")
        if vid is not None and vid.isOpened():
            vid.release()
        vid = cv2.VideoCapture(vid_source)

        #making changes in the buttons text and color
        if vid.isOpened():
            is_capturing = True
            btn_capture.config(text="Stop", bg="light coral")
            capture_thread = threading.Thread(target=capture_thread)
            capture_thread.start()
    except Exception as e:
        print(f"3.{e}")

#updates the image shown on the canvas
def update():
    try:
        global is_capturing, canvas, photo, vid
        if is_capturing:
            ret, frame = vid.read()
            if ret:
                # Make detections
                results = model(frame)
                boxes, colors, names = parse_detections(results)
                frame = draw_detections(boxes, colors, names, frame)
                
                photo = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
                canvas.create_image(0, 0, image=photo, anchor=tk.NW)
        window.after(10, update)
    except Exception as e:
        print(f"4.{e}")

#captures the frames in a seperate thread to avoid long delat and crash 
def capture_thread():
    try:
        global is_capturing, vid
        while is_capturing and vid.isOpened():
            ret, frame = vid.read()
            if ret:
                # Make detections
                results = model(frame)
                boxes, colors, names = parse_detections(results)
                frame = draw_detections(boxes, colors, names, frame)
                
                cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                photo = ImageTk.PhotoImage(image=Image.fromarray(cv2image))
                canvas.create_image(0, 0, image=photo, anchor=tk.NW)
        
        if vid.isOpened():
            vid.release()
    except Exception as e:
        print(f"5.{e}")

#works wehn Capture/Stop button is clicked
def toggle_capture():
    try:
        global is_capturing, btn_capture, vid, vid_source
        if is_capturing:
            is_capturing = False
            btn_capture.config(text="Capture", bg="light green")
            canvas.delete("all")
        else:
            vid_source = 0
            vid = cv2.VideoCapture(vid_source)
            if vid.isOpened():
                is_capturing = True
                btn_capture.config(text="Stop", bg="light coral")
                capture_thread = threading.Thread(target=capture_thread)
                capture_thread.start()
    except Exception as e:
        print(f"6.{e}")

#releases all the resources (camera and other) when the application is closed
def on_close():
    try:
        global is_capturing, vid
        is_capturing = False
        if vid is not None and vid.isOpened():
            vid.release()
        window.destroy()
    except Exception as e:
        print(f"7.{e}")

# Creating the main window
window = tk.Tk()
window.title("Akshadrik")

top_frame = tk.Frame(window)

title1_L = tk.Label(top_frame, text="Object", font=("Roquen", 19, "bold"))
title1_L.pack(anchor="nw")
title2_L = tk.Label(top_frame, text="Detection", font=("Roquen", 19, "bold"))
title2_L.pack(anchor="nw")
creatorreport_L = tk.Label(top_frame, text="Kewal Shah | Version: 1.0.3", font=("Calibri", 7, "bold"))
creatorreport_L.pack(anchor="nw")

separator2_frame = tk.Frame(top_frame, height=3, bd=1, relief=tk.SUNKEN)
separator2_frame.pack(fill='x', pady=5)

entry_source = tk.Entry(top_frame, width=23)
entry_source.insert(0, "0")
entry_source.pack(pady=5)
btn_set_source = tk.Button(top_frame, text="Set Video Source", command=set_vid_source)
btn_set_source.pack(pady=5)

separator_frame = tk.Frame(top_frame, height=3, bd=1, relief=tk.SUNKEN)
separator_frame.pack(fill='x', pady=5)

detection_source = tk.Entry(top_frame, width=23)
detection_source.insert(0, "person")
detection_source.pack(pady=5)
detection_L = tk.Label(top_frame, text="Detection Item")
detection_L.pack(pady=5)
item_frame = tk.Frame(top_frame)
item_list = tk.Listbox(item_frame,
    height=11,
    width=25,
    bd=0,
    highlightthickness=0,
    activestyle="none"
)
items = ['(None)', 'airplane', 'backpack', 'bed', 'bench', 'bicycle', 'boat', 'bus', 'car', 'cat', 'cell phone', 'chair', 'couch', 'dining table', 'dog', 'elephant', 'fire hydrant', 'fork', 'horse', 'keyboard', 'kite', 'knife', 'laptop', 'microwave', 'motorcycle', 'mouse', 'person', 'refrigerator', 'remote', 'scissors', 'skateboard', 'stop sign', 'suitcase', 'traffic light', 'train', 'truck', 'tv', 'umbrella']
for item in items:
    item_list.insert(tk.END, item)
item_list.pack(side=tk.LEFT, fill=tk.BOTH)
scrollbar = tk.Scrollbar(top_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
item_list.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=item_list.yview)
item_frame.pack()

top_frame.pack(side=tk.LEFT, pady=10, padx=2)

#used to get the selected item from the listbox
def selection(event):
    selected_item = item_list.get(item_list.curselection())
    detection_source.delete(0, tk.END)
    detection_source.insert(0, selected_item)
    
item_list.bind('<<ListboxSelect>>', selection)

frame_canvas = tk.Frame(window, borderwidth=1, relief="sunken")
frame_canvas.pack(padx=5)

canvas = tk.Canvas(frame_canvas, width=640, height=480)  
canvas.pack()

is_capturing = False
btn_capture = tk.Button(window, text="Capture", width=10, command=toggle_capture, bg="light green", font=("Calibri", 15, "bold"))
btn_capture.pack(pady=10)

photo = None

#loading the model
try:
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
except Exception as e:
    print(f"Model Loading: {e}")

# Register the on_close function to be called when the window is closed
window.protocol("WM_DELETE_WINDOW", on_close)

window.after(10, update)
window.mainloop()
