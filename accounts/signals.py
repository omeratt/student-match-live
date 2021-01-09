from django.db.models.signals import post_save
from django.contrib.auth.models import User
# from .models import User
from django.dispatch import receiver
# from .models import Profile,Student
from .models import Student,Teacher
# signal that gets fired after the user is saved
# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
#
# @receiver(post_save, sender=User)
# def save_profile(sender, instance, **kwargs):
#     instance.profile.save()

# ========================= student ======================
# @receiver(post_save, sender=User)
# def create_Student(sender, instance, created, **kwargs):
#     print(sender)
#     print(instance)
#     if created:
#         Student.objects.create(user=instance)
#
#
# @receiver(post_save, sender=User)
# def save_Student(sender, instance, **kwargs):
#     instance.student.save()
#
#
# # ========================= teacher ======================
# @receiver(post_save, sender=User)
# def create_teacher(sender, instance, created, **kwargs):
#     print(sender)
#     print(instance)
#     if created:
#         Teacher.objects.create(user=instance)
#
#
# @receiver(post_save, sender=User)
# def save_teacher(sender, instance, **kwargs):
#     instance.teacher.save()

# @receiver(post_save, sender=Student)
# def create_or_update_user_profile(sender, instance, created, **kwargs):
#
#     """
#     sender: sender model from which you'll receive signal from
#     instance: model instance(record) which is saved (it will be instance of sender model)
#     """
#     print("asdasdasd")
#     # teacher = Teacher.objects.create(user=instance)
#     if created:
#         print("asdasdasd")
#           # used to perform action only at creation time (avoid the code to execute during any update)
#         if instance.is_student:  # access the field of instance
#             print("asdasdasd")
#             student = Student.objects.create(user=instance) # you have correctly passed instance to foreign key and you just need to check condition for the same
#         #
#         else:
#             print("asdasdasd")
#             teacher = Teacher.objects.create(user=instance)
#             instance.teacher.save()


#
# @receiver(post_save, sender=User)
# def save_teacher(sender, instance, **kwargs):
#     instance.teacher.save()
# @receiver(post_save, sender=User)
# def save_teacher(sender, instance, **kwargs):
#     instance.teacher.save()
