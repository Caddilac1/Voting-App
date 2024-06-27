from django.urls import path 
from . import views


urlpatterns = [
    path('',views.project1,name = "Login Page"),
    
    path('project2/',views.project2,name = "Voting page 1"),
    
    path('project30/',views.project30,name = "Voting page 2"),
    
    path('project3/',views.project3,name = "Voting page 3"),
    
    path('project4/',views.project4,name = "Voting page 4"),
    
    path('project5/',views.project5,name = "Voting page 5"),
    
    path('project6/',views.project6,name = "Voting page 6"),
    
    path('project7/',views.project7,name = "Voting page 7"),
    
    path('project8/',views.project8,name = "Voting page 8"),
    
    path('project9/',views.project9,name = "Voting page 9"),
    
    path('project10/',views.project10,name = "Voting page 10"),
    
    path('project11/',views.project11,name = "Voting page 11"),
    
    path('project12/',views.project12,name = "Voting page 12"),
    
    path('project13/',views.project13,name = "Voting page 13"),
    
    path('project14/',views.project14,name = "Voting page 14"),
    
    path('project15/',views.project15,name = "Voting page 15"),
    
    path('project16/',views.project16,name = "Voting page 16"),
    
    path('project17/',views.project17,name = "Voting page 17"),
    
    path('project18/',views.project18,name = "Voting page 18"),
    
    path('project19/',views.project19,name = "Voting page 19"),
    
    path('project20/',views.project20,name = "Voting page 20"),
    
    path('project21/',views.project21,name = "Exit Page"),

    path('cast_vote/', views.cast_vote, name='cast_vote'),
    
    path('my-view/',views.my_view, name='my-view')

]
