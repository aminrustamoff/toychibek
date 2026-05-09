from django.db import models


class Comments(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ism")
    message = models.TextField(verbose_name="Xabar")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Izoh"
        verbose_name_plural = "Izohlar"

    def __str__(self):
        return f"{self.name} - {self.created_at.strftime('%d.%m.%Y')}"


class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ism")
    email = models.EmailField(max_length=100, verbose_name="Email")
    message = models.TextField(verbose_name="Xabar")
    is_read = models.BooleanField(default=False, verbose_name="O'qilgan")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Murojaat"
        verbose_name_plural = "Murojaatlar"

    def __str__(self):
        return f"{self.name} - {self.email}"


class Project(models.Model):
    STATUS_CHOICES = [
        ('active', 'Faol'),
        ('sold_out', 'Tugagan'),
        ('upcoming', 'Kutilmoqda'),
    ]

    image = models.ImageField(upload_to='project_images/', verbose_name="Rasm")
    name = models.CharField(max_length=100, verbose_name="Nomi")
    description = models.TextField(verbose_name="Tavsif")
    rooms = models.IntegerField(verbose_name="Xonalar soni")
    floor = models.IntegerField(verbose_name="Qavatlar soni")
    location = models.CharField(max_length=100, verbose_name="Joylashuv")
    available_numbers = models.IntegerField(verbose_name="Bo'sh xonalar")
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Narx ($)")
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='active',
        verbose_name="Holati"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Loyiha"
        verbose_name_plural = "Loyihalar"

    def __str__(self):
        return self.name


class Lead(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ism")
    phone = models.CharField(max_length=30, verbose_name="Telefon")
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE,
        related_name='leads',
        verbose_name="Loyiha"
    )
    is_contacted = models.BooleanField(default=False, verbose_name="Bog'lanildi")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Ariza"
        verbose_name_plural = "Arizalar"

    def __str__(self):
        return f"{self.name} - {self.phone}"


class AdminPanel(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nomi")
    budget = models.DecimalField(max_digits=14, decimal_places=2, verbose_name="Byudjet ($)")
    note = models.TextField(blank=True, null=True, verbose_name="Izoh")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Byudjet"
        verbose_name_plural = "Byudjetlar"

    def __str__(self):
        return f"{self.name} - ${self.budget}"