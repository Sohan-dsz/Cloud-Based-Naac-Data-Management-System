from django.contrib.auth.models import AbstractUser
from django.db import models
from simple_history.models import HistoricalRecords

class User(AbstractUser):
    """Extended User model with NAAC-specific fields"""
    
    ROLE_CHOICES = [
        ('iqac_admin', 'IQAC Administrator'),
        ('dept_admin', 'Department Administrator'),
        ('faculty', 'Faculty Member'),
        ('student', 'Student'),
    ]
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='faculty')
    employee_id = models.CharField(max_length=50, unique=True, null=True, blank=True)
    department = models.CharField(max_length=100, blank=True)
    designation = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    
    # Keycloak integration fields
    keycloak_id = models.CharField(max_length=100, unique=True, null=True, blank=True)
    last_keycloak_sync = models.DateTimeField(null=True, blank=True)
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    # History tracking
    history = HistoricalRecords()
    
    class Meta:
        db_table = 'auth_user_extended'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def __str__(self):
        return f"{self.get_full_name()} ({self.username})"
    
    @property
    def full_name(self):
        return self.get_full_name()
    
    def has_role(self, role):
        """Check if user has specific role"""
        return self.role == role
    
    def is_admin(self):
        """Check if user is any kind of admin"""
        return self.role in ['iqac_admin', 'dept_admin']


class UserProfile(models.Model):
    """Extended profile information for users"""
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.TextField(blank=True)
    
    # Academic information
    qualification = models.CharField(max_length=200, blank=True)
    experience_years = models.IntegerField(null=True, blank=True)
    specialization = models.CharField(max_length=200, blank=True)
    
    # Social links
    linkedin_url = models.URLField(blank=True)
    orcid_id = models.CharField(max_length=50, blank=True)
    google_scholar_url = models.URLField(blank=True)
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # History tracking
    history = HistoricalRecords()
    
    class Meta:
        db_table = 'user_profiles'
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'
    
    def __str__(self):
        return f"Profile of {self.user.get_full_name()}"