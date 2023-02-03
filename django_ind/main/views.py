from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Painter, Picture, Gallery
from .forms import PainterForm, GalleryForm, PictureForm


def index(request):
    painters = Painter.objects.order_by('name')[:2]
    pictures = Picture.objects.order_by('name')[:2]
    galleries = Gallery.objects.order_by('name')[:2]
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'painters': painters,
                                               'pictures': pictures, 'galleries': galleries, })


def view_picture(request, picture_id):
    picture = get_object_or_404(Picture, pk=picture_id)
    return render(request, 'main/view_picture.html', {'picture': picture})


def view_pictures(request):
    # print(request.POST)
    # if all(['name' in request.POST, 'genre' in request.POST, 'year' in request.POST, 'painter' in request.POST, 'gallery' in request.POST ]):
    #     picture_painter = get_object_or_404(Painter, pk=request.POST['painter_id'])
    #     picture_gallery = get_object_or_404(Gallery, pk=request.POST['gallery_id'])
    #     picture = Picture(name=request.POST['name'], genre=request.POST['genre'], year=request.POST['year'],
    #                       painter=picture_painter, gallery=picture_gallery )
    #     picture.save()

    if request.method == 'POST':
        form = PictureForm(request.POST)
        if form.is_valid():
            form.save()
    pictures = Picture.objects.order_by('name')
    painters = Painter.objects.order_by('name')
    galleries = Gallery.objects.order_by('name')

    form = PictureForm()
    form_painter = PainterForm
    form_gallery = GalleryForm
    return render(request, 'main/view_pictures.html', {'pictures': pictures, 'painters': painters,
                    'galleries': galleries, 'form': form, 'form_painter': form_painter, 'form_gallery': form_gallery})


def view_painters(request):
    if request.method == 'POST':
        form = PainterForm(request.POST)
        if form.is_valid():
            form.save()
    painters = Painter.objects.order_by('name')
    form = PainterForm()
    return render(request, 'main/view_painters.html', {'painters': painters, 'form': form})


def view_galleries(request):
    if request.method == 'POST':
        form = GalleryForm(request.POST)
        if form.is_valid():
            form.save()
    galleries = Gallery.objects.order_by('name')
    form = GalleryForm()
    return render(request, 'main/view_galleries.html', {'galleries': galleries, 'form': form})


def change_picture(request):
    picture = Picture.objects.get(id=request.GET['id'])
    picture.name = request.GET['name']
    picture.genre = request.GET['genre']
    picture.year = request.GET['year']
    picture.painter = Painter.objects.get(name=request.GET['painter'])
    picture.gallery = Gallery.objects.get(name=request.GET['gallery'])
    picture.save()
    return render(request, 'main/change_picture.html', {'picture': picture})


def change_gallery(request):
    gallery = Gallery.objects.get(id=request.GET['id'])
    gallery.name = request.GET['name']
    gallery.city = request.GET['city']
    gallery.country = request.GET['country']
    gallery.save()
    return render(request, 'main/change_gallery.html', {'gallery': gallery})


def change_painter(request):
    painter = Painter.objects.get(id=request.GET['id'])
    painter.name = request.GET['name']
    painter.country = request.GET['country']
    painter.save()
    return render(request, 'main/change_painter.html', {'painter': painter})


def thanks(request):
    name = request.GET['name']
    genre = request.GET['genre']
    year = request.GET['year']
    painter = request.GET['painter']
    gallery = request.GET['gallery']
    picture = Picture(name=name, genre=genre, year=year, painter=Painter.objects.get(name=painter), gallery=Gallery.objects.get(name=gallery))
    picture.save()
    return render(request, 'main/thanks.html')