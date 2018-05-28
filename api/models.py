from django.db import models

class Bucketlist(models.Model):
    """This class represents the bucketlist model."""
    accuracy = models.CharField(max_length=255, blank=False, unique=True)
    no_of_batches = models.CharField(max_length=255, blank=False, unique=True)
    itera = models.CharField(max_length=255, blank=False, unique=True)
    lear_rate = models.CharField(max_length=255, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.accuracy)
        return "{}".format(self.no_of_batches)
        return "{}".format(self.itera)
        return "{}".format(self.lear_rate)
