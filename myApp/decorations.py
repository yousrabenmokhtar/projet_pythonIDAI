from django.http import HttpResponse , HttpResponseForbidden
from django.shortcuts import redirect



def unauthenticatedUser(view_func):
  def wrapper_func(request , *args , **kwargs):
    if request.user.is_authenticated:
     return redirect('home')
    
    else:
      return view_func(request , *args , **kwargs)
    
  
  return wrapper_func


# def allowed_users(allowed_roles=[]):
#   def decorator(view_func):
#     def wrapper_func(request , *args , **kwargs):
#       group = None

#       if request.user.groups.exists():
#         group = request.user.groups.all()[0].name

#       if group in allowed_roles:
#         return view_func(request , *args , **kwargs)
#       # elif group is None:

#       #   return HttpResponse("You are not authorized to see this page !")
#       else:
#         return HttpResponse("You are not authorized to see this page !")
      
   
#     return wrapper_func
#   return decorator


# def onlyAdmins(view_func):
#     def wrapper_func(request, *args, **kwargs):
#         group = None

#         if request.user.groups.exists():
#             group = request.user.groups.all()[0].name

#         if group == 'Etudiant':
#             return redirect('settProfile')
#         if group == 'Professeur':
#             return redirect('settProfileProf')
#         if group == 'Entreprise':
#             return redirect('settProfileEnt')
        
#         if group == 'admin':  
#             return view_func(request, *args, **kwargs)

#     return wrapper_func