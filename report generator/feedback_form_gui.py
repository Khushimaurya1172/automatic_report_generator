import tkinter as tk
from tkinter import messagebox
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os
import webbrowser

def generate_feedback_pdf():
    name = name_entry.get()
    email = email_entry.get()
    feedback = feedback_text.get("1.0", "end").strip()
    rating = rating_entry.get()
    suggestions = suggestion_text.get("1.0", "end").strip()

    if not name or not email or not feedback or not rating:
        messagebox.showerror("Error", "Please fill all required fields.")
        return

    # Create directory on Desktop
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    feedback_dir = os.path.join(desktop_path, "feedbacks")
    os.makedirs(feedback_dir, exist_ok=True)

    filename = f"Feedback_{name.replace(' ', '_')}.pdf"
    filepath = os.path.join(feedback_dir, filename)

    # Generate PDF
    c = canvas.Canvas(filepath, pagesize=A4)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(200, 800, "Intern Feedback Form")

    c.setFont("Helvetica", 12)
    c.drawString(50, 760, f"Name: {name}")
    c.drawString(50, 740, f"Email: {email}")
    c.drawString(50, 720, f"Rating (1-5): {rating}")
    c.drawString(50, 700, "Feedback:")
    text_obj = c.beginText(60, 680)
    text_obj.textLines(feedback)
    c.drawText(text_obj)

    if suggestions:
        c.drawString(50, 640 - (len(feedback.splitlines()) * 12), "Suggestions:")
        suggestion_obj = c.beginText(60, 620 - (len(feedback.splitlines()) * 12))
        suggestion_obj.textLines(suggestions)
        c.drawText(suggestion_obj)

    c.save()

    messagebox.showinfo("Success", f"Feedback saved as PDF:\n{filepath}")
    webbrowser.open_new(filepath)

# GUI Setup
root = tk.Tk()
root.title("Intern Feedback Form")
root.geometry("600x600")

tk.Label(root, text="Name *").grid(row=0, column=0, sticky="w", padx=10, pady=5)
name_entry = tk.Entry(root, width=50)
name_entry.grid(row=0, column=1, pady=5)

tk.Label(root, text="Email *").grid(row=1, column=0, sticky="w", padx=10)
email_entry = tk.Entry(root, width=50)
email_entry.grid(row=1, column=1)

tk.Label(root, text="Feedback *").grid(row=2, column=0, sticky="nw", padx=10, pady=5)
feedback_text = tk.Text(root, width=38, height=5)
feedback_text.grid(row=2, column=1)

tk.Label(root, text="Rating (1 to 5) *").grid(row=3, column=0, sticky="w", padx=10, pady=5)
rating_entry = tk.Entry(root, width=10)
rating_entry.grid(row=3, column=1, sticky="w")

tk.Label(root, text="Suggestions (Optional)").grid(row=4, column=0, sticky="nw", padx=10, pady=5)
suggestion_text = tk.Text(root, width=38, height=4)
suggestion_text.grid(row=4, column=1)

submit_btn = tk.Button(root, text="Generate Feedback PDF", command=generate_feedback_pdf, bg="#4CAF50", fg="white", width=30)
submit_btn.grid(row=5, column=1, pady=20)

root.mainloop()
