from django.contrib.auth.mixins import UserPassesTestMixin

class ProviderRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_provider
    
class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_admin or self.request.user.is_superuser
    
class ReviewOwnerOrAdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        review = self.get_object()
        return self.request.user == review.user or self.request.user.is_superuser or self.request.user.is_admin