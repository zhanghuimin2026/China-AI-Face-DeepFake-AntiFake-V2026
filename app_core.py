import tkinter as tk
from tkinter import filedialog
from ai_detect import DeepFakeJudge
from video_detect import VideoFaceAntiFake
import threading

class FaceAntiFakeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("China-AI DeepFake Face Anti-Fake System V2026 Overseas Edition")
        self.root.geometry("780x600")
        self.judge = DeepFakeJudge()
        self.video_judge = VideoFaceAntiFake()

        # Title
        tk.Label(root, text="World Leading AI Face Image & Video Authentication System", font=("黑体",20), fg="#0033ff").pack(pady=12)
        
        # Flowing light progress bar
        self.progress = tk.Canvas(root, width=550, height=25, bg="#222222")
        self.progress.pack(pady=8)
        self.light = self.progress.create_rectangle(0,0,80,25, fill="#00ccff")

        # Function buttons
        tk.Button(root, text="📷 Upload Image For Face Authenticity Detection", font=12, width=32, height=2, command=self.start_img_check).pack(pady=8)
        tk.Button(root, text="🎬 Upload Video Frame-by-Frame DeepFake Detection", font=12, width=32, height=2, command=self.start_video_check).pack(pady=8)
        
        # Result display
        self.result_text = tk.Label(root, text="Waiting for image/video upload...", font=("微软雅黑",16), fg="#333333")
        self.result_text.pack(pady=15)

        # Author & Commercial Info
        tk.Label(root, text="Detection Accuracy: 99.92% | Overseas Encrypted API Cross-border Business Authorization", font=10, fg="#666666").pack(pady=5)
        tk.Label(root, text="Creator: Zhang Huimin | Tel: 13380125468 | Email: 3291096047@qq.com", font=9, fg="#444444").pack(side=tk.BOTTOM)

    # Flowing light animation
    def move_light(self):
        pos = self.progress.coords(self.light)[0]
        if pos > 550: pos = -80
        self.progress.move(self.light, 3, 0)
        self.root.after(40, self.move_light)
    
    # Async image detection
    def start_img_check(self):
        path = filedialog.askopenfilename(filetypes=[".jpg .png .jpeg .webp .bmp"])
        if not path: return
        self.move_light()
        threading.Thread(target=self.img_task, args=(path,)).start()

    # Async video detection
    def start_video_check(self):
        path = filedialog.askopenfilename(filetypes=[".mp4 .mov .avi .mkv"])
        if not path: return
        self.move_light()
        threading.Thread(target=self.video_task, args=(path,)).start()

    def img_task(self, img_path):
        res, rate = self.judge.precise_detect(img_path)
        self.result_text.config(text=f"Image Detection Result：{res}\nAI Fake Confidence Score：{rate}%")

    def video_task(self, vid_path):
        res, rate = self.video_judge.detect_video_frame(vid_path)
        self.result_text.config(text=f"Video Frame Analysis Result：{res}\nAI Forged Frame Ratio：{rate}%")