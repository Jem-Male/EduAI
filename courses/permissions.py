from rest_framework import permissions


class IsAdminOrTeacherOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view): # type: ignore 
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return bool(request.user and request.user.is_staff)
    
    def has_object_permission(self, request, view, obj): # type: ignore
        if request.method in permissions.SAFE_METHODS:
            return True
        
        if request.user.is_superuser:
            return True
        
        if hasattr(obj, 'creator'):
            return obj.creator == request.user
        
        if hasattr(obj, 'course'):
            return obj.course.creator == request.user
        
        if hasattr(obj, 'quiz'):
            return obj.quiz.course.creator == request.user
        
        return False


class IsSolver(permissions.BasePermission):
    def has_permission(self, request, view): # type: ignore
        return (
            request.user.is_authenticated
            and request.method in ['GET', 'HEAD', 'OPTIONS', 'POST']
        )