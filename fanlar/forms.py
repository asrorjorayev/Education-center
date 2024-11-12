from django import forms
from .models import RegisterKurs

class RegisterCourseForm(forms.ModelForm):
    class Meta:
        model = RegisterKurs
        fields = ["ism", "familya", "phone", "kurs", "dars_kunlari", "izoh"]

    def clean_ism(self):
        ism = self.cleaned_data.get("ism")
        if not isinstance(ism, str) or not ism.isalpha():
            raise forms.ValidationError("Ismni faqat harflar bilan kiriting.")
        return ism

    def clean_familya(self):
        familya = self.cleaned_data.get("familya")
        if not isinstance(familya, str) or not familya.isalpha():
            raise forms.ValidationError("Familyani faqat harflar bilan kiriting.")
        return familya

        