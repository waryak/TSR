from django.db import models


class Organisation(models.Model):
    organisation_name = models.CharField(max_length=200, primary_key=True)
    organisation_type = models.CharField(max_length=100)
    organisation_city = models.CharField(max_length=100)


class Trajectories(models.Model):
    organisation_name = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    trajectory_name = models.CharField(max_length=200)
    trajectory_type = models.CharField(max_length=100)
    node_id = models.IntegerField()


class Steps(models.Model):
    step_name = models.CharField(max_length=200)
    parent_step_id = models.IntegerField()


class Nodes(models.Model):
    node_name = models.CharField(max_length=200, primary_key=True)
    step_id = models.ForeignKey(Steps, on_delete=models.CASCADE)


class TrajectoryNodes(models.Model):
    traj_id = models.ForeignKey(Trajectories, on_delete=models.CASCADE)
    node_id = models.ForeignKey(Nodes, on_delete=models.CASCADE)


class Student(models.Model):
    student_id = models.IntegerField()
    student_name = models.CharField(max_length=200)
