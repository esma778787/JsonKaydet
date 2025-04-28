import json
import csv

class Student:
    def __init__(self):
        self.student = {
            "ad": "",
            "no": None,
            "dersler": {}
        }
        self.get_student_info()
        self.get_course_info()
        self.save_to_json()
        mixed_data = self.swap_scores()
        self.save_to_csv(mixed_data)

    def get_student_info(self):
        self.student["ad"] = input("Adınız: ")
        while self.student["no"] is None:
            try:
                self.student["no"] = int(input("Numaranız: "))
            except ValueError:
                print("Numara sayı olmalı!")

    def get_course_info(self):
        for _ in range(7):
            course_name = input("Ders adı: ")
            course = {"vize": None, "final": None}
            while course["vize"] is None:
                try:
                    course["vize"] = float(input(f"{course_name} vize notu: "))
                except ValueError:
                    print("Vize notu sayı olmalı!")
            while course["final"] is None:
                try:
                    course["final"] = float(input(f"{course_name} final notu: "))
                except ValueError:
                    print("Final notu sayı olmalı!")
            self.student["dersler"][course_name] = course

    def save_to_json(self):
        with open("student.txt", "w", encoding="utf-8") as file:
            json.dump(self.student, file, ensure_ascii=False)

    def read_from_json(self):
        with open("student.txt", "r", encoding="utf-8") as file:
            return json.load(file)

    def swap_scores(self):
        data = self.read_from_json()
        for course in data["dersler"]:
            vize = data["dersler"][course]["vize"]
            final = data["dersler"][course]["final"]
            data["dersler"][course]["vize"], data["dersler"][course]["final"] = final, vize
        return data

    def save_to_csv(self, data):
        courses = data.pop("dersler")
        with open("student.csv", "w", newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Field", "Value"])
            for key, value in data.items():
                writer.writerow([key, value])
            writer.writerow(["Course", "Vize", "Final"])
            for course_name, grades in courses.items():
                writer.writerow([course_name, grades["vize"], grades["final"]])

# Programı başlat
Student()
