import os
from django.conf import settings
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from faker import Faker
from .models import *
from random import randint

# Create your views here.
def index(request):
	paginator =Paginator(Article.objects.filter(status=True).order_by('-date_add'),6)
	if request.method == 'GET':
		page=request.GET.get('page',1)
	articles = paginator.page(page)
	data = {
		'category':Categorie.objects.filter(status=True),
		'articles':articles,
	}
	return render(request,'pages/blog.html', data)

def article(request, id):
	data = {
		'category':Categorie.objects.filter(status=True),
		'article':Article.objects.get(pk=id),
	}
	return render(request,'pages/single_blog.html', data)



def artFake(request):
	from django.core.files import File
	fake = Faker()
	category = Categorie.objects.filter(status=True)
	tag=Tag.objects.filter(status=True)
	auteur = Author.objects.get(pk=1)
	images = [os.path.join(settings.BASE_DIR,'static/images/breakfast-'+str(i)+'.jpg') for i in range(1,5)]+ [os.path.join(settings.BASE_DIR,'static/images/lunch-'+str(i)+'.jpg') for i in range(1,5)] + [os.path.join(settings.BASE_DIR,'static/images/dinner-'+str(i)+'.jpg') for i in range(1,5)] + [os.path.join(settings.BASE_DIR,'static/images/dessert-'+str(i)+'.jpg') for i in range(1,5)] + [os.path.join(settings.BASE_DIR,'static/images/drink-'+str(i)+'.jpg') for i in range(1,6)]
	inter=0
	while inter < 100:
		cat = category[randint(0,len(category)-1)]
		inter += 1
		art = Article(
			titre=fake.sentence(nb_words=15, variable_nb_words=True, ext_word_list=None),
			description= fake.paragraph(nb_sentences=3, variable_nb_sentences=True, ext_word_list=None),
			contenu=fake.text(max_nb_chars=800, ext_word_list=None),
			categorie= cat,
			author=auteur,
			acceuil= fake.boolean(),
		)
		img=images[randint(0,len(images)-1)]
		img = open(img,'rb')
		name='{}.jpg'.format(cat.titre)
		art.image.save(name, File(img))
		for t in tag:
			art.tag.add(t)
		art.save()
	return redirect('blog:index')

