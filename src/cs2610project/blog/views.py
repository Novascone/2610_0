from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from time import strftime
from .models import Blog, Comment
from django.utils import timezone
# Create your views here.
def index(request):
    return render(request,'blog/blog.html', {'now': strftime('%c')})

def bio(request):
    return render(request,'blog/bio.html', {'now': strftime('%c')})

def tips(request):
    return render(request,'blog/tips.html', {'now': strftime('%c')})

def BlogHome(request):
    last = Blog.objects.order_by('-post_date')[:3]
    context = {'last':last}
    return render(request, 'blog/BlogHome.html',context)

def BlogArchive(request):
    last = Blog.objects.order_by('-post_date')
    context = {'last':last}
    return render(request, 'blog/BlogArchive.html',context)

def BlogEntry(request, b_id):
    blog = get_object_or_404(Blog, pk=b_id)
    lastC = Comment.objects.order_by('-post_date')
    return render(request,'blog/BlogEntry.html',{'blog':blog})

def nuke(request):
    for blog in Blog.objects.all():
        blog.delete()
    return HttpResponseRedirect(reverse('blog:bloghome'))

def postComment(request,b_id):
    blog = get_object_or_404(Blog, pk=b_id)
    comment = Comment(
        blog = blog,
        nickname = request.POST['nickname'],
        email = request.POST['email'],
        content = request.POST['content'],
        post_date = timezone.now()
        )
    comment.save()
    return HttpResponseRedirect(reverse('blog:entry', args=(b_id,)))
                      


def init(request):
    nuke(request)
    
    for i in range(6):
        blog = Blog(
        title = "Blog" + str(i),
        author_name = "dave",
        content = " Cras nec ex sagittis, semper eros eu, placerat erat. Integer nec mi sed nunc tristique vestibulum efficitur vitae erat. Nullam cursus quis ante sed aliquam. Morbi     porttitor bibendum pretium. Mauris cursus tortor eu nulla placerat, quis venenatis odio lacinia. Sed placerat aliquet elit non sollicitudin. Maecenas sed interdum libero. Maecenas bibendum leo et facilisis rutrum. Aliquam lectus dui, imperdiet et interdum lobortis, faucibus non dui. Sed nisl felis, interdum mollis est nec, varius condimentum erat. Pellentesque condimentum accumsan facilisis. Duis sed lacus sit amet sem gravida dictum in eu sem. Pellentesque dictum erat id augue porttitor placerat sit amet ut elit. Aenean elit quam, consectetur ac libero in, tempus lacinia diam.Sed a egestas est. \Maecenas sollicitudin pharetra nulla. Curabitur elementum purus at leo rutrum ornare. Ut a nibh tincidunt, aliquet turpis sed, hendrerit magna. Nullam ornare condimentum magna, vel vestibulum nulla. Vivamus in nisl purus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sollicitudin neque vitae nisl pellentesque auctor. Vivamus in dapibus ante. Sed tellus ipsum, laoreet quis augue nec, ultrices semper odio. Nullam vitae elit fringilla, tempus est a, tempor lacus.\Vestibulum tincidunt tortor ac volutpat mattis. Fusce convallis dolor nisl, vitae scelerisque enim tristique eget. Sed bibendum tempor justo, ut viverra magna finibus in. Quisque urna diam, hendrerit sed sagittis in, volutpat id neque. Mauris eget molestie risus. Aenean ut nunc libero. Aliquam tempor lorem nisl, malesuada cursus risus consectetur at. Pellentesque sollicitudin consectetur velit quis placerat. Nunc eget quam a mauris aliquam pellentesque ut nec turpis. Sed nulla diam, tincidunt euismod odio ac, auctor pulvinar ante. Phasellus vel augue gravida, fermentum nisl ac, convallis tortor. Vestibulum eu scelerisque nibh. Pellentesque justo diam, vestibulum ut felis ut, convallis tempus sem. Donec feugiat risus non felis vehicula viverra. Nam dignissim ut purus a viverra. Sed accumsan lectus sed massa dictum fringilla.",
        post_date = timezone.now()
         )
        blog.save()
        for j in range(5):
            comment = Comment(blog = blog,
                nickname = "nick",
                email = "nick@gmail.com",
                content = "Cras nec ex sagittis, semper eros eu, placerat erat. Integer nec mi sed nunc tristique vestibulum efficitur vitae erat. Nullam cursus quis ante sed aliquam. Morbi     porttitor bibendum pretium. Mauris cursus tortor eu nulla placerat, quis venenatis odio lacinia. Sed placerat aliquet elit non sollicitudin. Maecenas sed interdum libero. Maecenas bibendum leo et facilisis rutrum. Aliquam lectus dui, imperdiet et interdum lobortis, faucibus non dui. Sed nisl felis, interdum mollis est nec, varius condimentum erat. Pellentesque condimentum accumsan facilisis. Duis sed lacus sit amet sem gravida dictum in eu sem. Pellentesque dictum erat id augue porttitor placerat sit amet ut elit. Aenean elit quam, consectetur ac libero in, tempus lacinia diam.",
                post_date = timezone.now()
                )
            comment.save()
    return HttpResponseRedirect(reverse('blog:bloghome'))



