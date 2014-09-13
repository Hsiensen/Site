#coding:utf-8
from django.db import models

class Index(models.Model):
	courses		= models.CharField(max_length=1024,blank=True,null=True)#主要课程
	cou_remarks	= models.TextField(blank=True,null=True)#主要课程备注
	liv_remarks	= models.TextField(blank=True,null=True)#公益直播备注
	str_remarks	= models.TextField(blank=True,null=True)#学生作品整体备注
	placement	= models.CharField(max_length=1024,blank=True,null=True)#分班时间,分班课程,分班人数
	scl_notes	= models.TextField(blank=True,null=True)#入学须知
	help		= models.TextField(blank=True,null=True)#帮助

class Courses(models.Model):
	cou_theme	= models.CharField(max_length=1024,blank=True,null=True)#授课主题
	cou_topic	= models.CharField(max_length=1024,blank=True,null=True)#授课题目
	cou_content	= models.TextField(blank=True,null=True)#授课内容
	bro	= models.IntegerField(default=1)#浏览数
	
class Student(models.Model):
	stu_name	= models.CharField(max_length=1024,blank=True,null=True)#学生姓名
	wor_introduc	= models.TextField(blank=True,null=True)#学生单个作品简介
	stu_photo	= models.ImageField(upload_to = 'photo',blank=True,null=True)#学生作品图片
	def photo_tag(self):
		if self.photo.name[0] == '/':
			return u'<img src="%s" />' % self.photo
		return u'<img style="width:50px; height:50px;"src="/static/%s" />' % self.photo
	photo_tag.short_description = 'Image'
	photo_tag.allow_tags = True

class Taped(models.Model):
	mov_remarks	= models.TextField(blank=True,null=True)#视频备注
	mov_photo	= models.ImageField(upload_to = 'photo',blank=True,null=True)#讲课视频图片
	def photo_tag(self):
		if self.photo.name[0] == '/':
			return u'<img src="%s" />' % self.photo
		return u'<img style="width:50px; height:50px;"src="/static/%s" />' % self.photo
	photo_tag.short_description = 'Image'
	photo_tag.allow_tags = True

class Live(models.Model):
	liv_remarks	= models.TextField(blank=True,null=True)#直播流程简介
	upc_content	= models.TextField(blank=True,null=True)#即将直播课程内容
	bei_content	= models.TextField(blank=True,null=True)#正在直播课程内容
	has_content	= models.TextField(blank=True,null=True)#已经直播课程内容
	mov_remarks	= models.TextField(blank=True,null=True)#直播作品备注
	mov_photo	= models.ImageField(upload_to = 'photo',blank=True,null=True)#往期直播视频图片
	def photo_tag(self):
		if self.photo.name[0] == '/':
			return u'<img src="%s" />' % self.photo
		return u'<img style="width:50px; height:50px;"src="/static/%s" />' % self.photo
	photo_tag.short_description = 'Image'
	photo_tag.allow_tags = True

class Ready(models.Model):
	ins_linux	= models.TextField(blank=True,null=True)#环境安装
	ins_mak		= models.TextField(blank=True,null=True)#环境安装
	ins_windows	= models.TextField(blank=True,null=True)#环境安装

##########################################################################################################
class TextInfo(models.Model):
	text		= models.TextField(blank=True,null=True)#不常修改文本
	tagname		= models.CharField(max_length=1024,blank=True,null=True)

class ImgInfo(models.Model):
	image		= models.ImageField(upload_to='image',blank=True,null=True)#不常修改图片
	tagname		= models.CharField(max_length=1024,blank=True,null=True)
	def image_tag(self):
		print self.image
		if self.image.name[0] == '/':
			return u'<img style="width:60px; height:60px;"src="%s" />' % self.image
		return u'<img style="width:60px; height:60px;"src="/static/%s" />' % self.image
	image_tag.short_description = 'Image'
	image_tag.allow_tags = True




