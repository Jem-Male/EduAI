from rest_framework import permissions

class IsAdminOrTeacherOrReadOnly(permissions.BasePermission):
    
    def has_permission(self, request, view): # type: ignore 
        if request.method == permissions.SAFE_METHODS:
            return True
        
        return bool(request.user and request.user.is_authenticated)
    
    def has_object_permission(self, request, view, obj): # type: ignore
        if request.method == permissions.SAFE_METHODS:
            return True
        
        if request.user.is_staff:
            return True
        
        if hasattr(obj, 'creater'):
            return obj.create == request.user
        
        if hasattr(obj, 'course'):
            return obj.course.creater == request.user
        
        if hasattr(obj, 'quiz'):
            return obj.quiz.course.creater == request.user
        
        return False