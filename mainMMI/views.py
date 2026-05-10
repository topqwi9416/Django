from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile, PracticeDocument, CharacteristicDocument, Document
import urllib.parse


def MainMMI(request):
    return render(request, 'main.html')


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')

    username = request.POST.get('username', '').strip()
    p1 = request.POST.get('password1', '')
    p2 = request.POST.get('password2', '')

    if not username:
        messages.error(request, 'Введите логин')
        return render(request, 'register.html')

    if p1 != p2:
        messages.error(request, 'Пароли не совпадают')
        return render(request, 'register.html')

    if len(p1) < 8:
        messages.error(request, 'Пароль должен быть не менее 8 символов')
        return render(request, 'register.html')

    if User.objects.filter(username=username).exists():
        messages.error(request, 'Пользователь с таким логином уже существует')
        return render(request, 'register.html')

    user = User.objects.create_user(username=username, password=p1)
    user.save()
    UserProfile.objects.get_or_create(user=user)
    login(request, user)
    return redirect('/profile/')


def loginf(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            UserProfile.objects.get_or_create(user=user)
            return redirect('/profile/')
        else:
            messages.error(request, 'Неверный логин или пароль')

    return render(request, 'login.html')


@login_required
def profile(request):
    prof, _ = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('firstName', '')
        user.last_name  = request.POST.get('lastName', '')
        user.email      = request.POST.get('email', '')
        user.save()

        prof.first_name  = request.POST.get('firstName', '')
        prof.last_name   = request.POST.get('lastName', '')
        prof.middle_name = request.POST.get('middleName', '')
        prof.phone       = request.POST.get('phone', '')
        prof.telegram    = request.POST.get('telegram', '')
        prof.birth_date  = request.POST.get('birthDate') or None
        prof.gender      = request.POST.get('gender', '')
        prof.inn         = request.POST.get('inn', '')
        prof.save()

        messages.success(request, 'Данные профиля успешно сохранены!')
        return redirect('/profile/')

    context = {
        'profile': prof,
        'user': request.user,
        'practice_docs': PracticeDocument.objects.filter(user=request.user),
        'characteristic_docs': CharacteristicDocument.objects.filter(user=request.user),
    }
    return render(request, 'profile.html', context)


@login_required
def create_practice_document(request):
    if request.method == 'POST':
        doc = PracticeDocument.objects.create(
            user=request.user,
            practice_type    = request.POST.get('practice_type', 'educational'),
            fio              = request.POST.get('fio', ''),
            speciality       = request.POST.get('speciality', ''),
            group            = request.POST.get('group', ''),
            course           = request.POST.get('course', ''),
            education_form   = request.POST.get('education_form', ''),
            start_date       = request.POST.get('start_date') or None,
            end_date         = request.POST.get('end_date') or None,
            organization     = request.POST.get('organization', ''),
            organization_address = request.POST.get('organization_address', ''),
            supervisor       = request.POST.get('supervisor', ''),
            module_code      = request.POST.get('module_code', ''),
            work_1_quality   = request.POST.get('work_1_quality', ''),
            work_2_quality   = request.POST.get('work_2_quality', ''),
            work_3_quality   = request.POST.get('work_3_quality', ''),
            work_4_quality   = request.POST.get('work_4_quality', ''),
            work_5_quality   = request.POST.get('work_5_quality', ''),
            work_6_quality   = request.POST.get('work_6_quality', ''),
            work_7_quality   = request.POST.get('work_7_quality', ''),
            work_8_quality   = request.POST.get('work_8_quality', ''),
            work_9_quality   = request.POST.get('work_9_quality', ''),
            work_10_quality  = request.POST.get('work_10_quality', ''),
            work_11_quality  = request.POST.get('work_11_quality', ''),
            pk_1_level       = request.POST.get('pk_1_level', ''),
            pk_2_level       = request.POST.get('pk_2_level', ''),
            pk_3_level       = request.POST.get('pk_3_level', ''),
            pk_4_level       = request.POST.get('pk_4_level', ''),
            pk_5_level       = request.POST.get('pk_5_level', ''),
            pk_6_level       = request.POST.get('pk_6_level', ''),
            ok_1_level       = request.POST.get('ok_1_level', ''),
            ok_2_level       = request.POST.get('ok_2_level', ''),
            ok_3_level       = request.POST.get('ok_3_level', ''),
            ok_4_level       = request.POST.get('ok_4_level', ''),
            ok_5_level       = request.POST.get('ok_5_level', ''),
            ok_6_level       = request.POST.get('ok_6_level', ''),
            ok_7_level       = request.POST.get('ok_7_level', ''),
            ok_8_level       = request.POST.get('ok_8_level', ''),
            ok_9_level       = request.POST.get('ok_9_level', ''),
            ok_10_level      = request.POST.get('ok_10_level', ''),
            ok_11_level      = request.POST.get('ok_11_level', ''),
            result           = request.POST.get('result', 'Программа практической подготовки выполнена в полном объёме'),
            document_date    = request.POST.get('document_date') or None,
        )
        messages.success(request, 'Аттестационный лист сохранён! Перейдите в «Мои документы» чтобы скачать.')
        return redirect('/profile/#my-docs')

    return redirect('/profile/')


@login_required
def create_characteristic_document(request):
    if request.method == 'POST':
        CharacteristicDocument.objects.create(
            user              = request.user,
            fio               = request.POST.get('fio', ''),
            library           = request.POST.get('library', ''),
            work_start        = request.POST.get('work_start') or None,
            work_end          = request.POST.get('work_end') or None,
            work_days_count   = request.POST.get('work_days_count') or None,
            missed_days       = request.POST.get('missed_days') or None,
            missed_unexcused  = request.POST.get('missed_unexcused') or None,
            speciality        = request.POST.get('speciality', ''),
            work_quality      = request.POST.get('work_quality', ''),
            supervisor        = request.POST.get('supervisor', ''),
        )
        messages.success(request, 'Характеристика сохранена! Перейдите в «Мои документы» чтобы скачать.')
        return redirect('/profile/#my-docs')

    return redirect('/profile/')


@login_required
def edit_practice_document(request, doc_id):
    doc = get_object_or_404(PracticeDocument, id=doc_id, user=request.user)

    if request.method == 'POST':
        doc.practice_type        = request.POST.get('practice_type', doc.practice_type)
        doc.fio                  = request.POST.get('fio', '')
        doc.speciality           = request.POST.get('speciality', '')
        doc.group                = request.POST.get('group', '')
        doc.course               = request.POST.get('course', '')
        doc.education_form       = request.POST.get('education_form', '')
        doc.start_date           = request.POST.get('start_date') or None
        doc.end_date             = request.POST.get('end_date') or None
        doc.organization         = request.POST.get('organization', '')
        doc.organization_address = request.POST.get('organization_address', '')
        doc.supervisor           = request.POST.get('supervisor', '')
        doc.module_code          = request.POST.get('module_code', '')
        for i in range(1, 12):
            setattr(doc, f'work_{i}_quality', request.POST.get(f'work_{i}_quality', ''))
        for i in range(1, 7):
            setattr(doc, f'pk_{i}_level', request.POST.get(f'pk_{i}_level', ''))
        for i in range(1, 12):
            setattr(doc, f'ok_{i}_level', request.POST.get(f'ok_{i}_level', ''))
        doc.result        = request.POST.get('result', '')
        doc.document_date = request.POST.get('document_date') or None
        doc.save()
        messages.success(request, 'Документ обновлён!')
        return redirect('/profile/#my-docs')

    return render(request, 'edit_practice_document.html', {'doc': doc})


@login_required
def delete_practice_document(request, doc_id):
    doc = get_object_or_404(PracticeDocument, id=doc_id, user=request.user)
    doc.delete()
    messages.success(request, 'Документ удалён!')
    return redirect('/profile/#my-docs')


@login_required
def view_practice_document(request, doc_id):
    doc = get_object_or_404(PracticeDocument, id=doc_id, user=request.user)
    return render(request, 'view_practice_document.html', {'doc': doc})


@login_required
def view_characteristic_document(request, doc_id):
    doc = get_object_or_404(CharacteristicDocument, id=doc_id, user=request.user)
    return render(request, 'view_characteristic_document.html', {'doc': doc})


# ─── Генерация и скачивание docx ─────────────────────────────────────────────

@login_required
def download_attestat(request, doc_id):
    from .docx_generator import generate_attestat
    doc    = get_object_or_404(PracticeDocument, id=doc_id, user=request.user)
    output = generate_attestat(doc)

    labels = {'educational': 'учебная', 'production': 'производственная', 'prediploma': 'преддипломная'}
    label  = labels.get(doc.practice_type, doc.practice_type)
    fname  = f'Аттестационный лист ({label}) - {doc.fio or "документ"}.docx'

    response = HttpResponse(
        output,
        content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    )
    response['Content-Disposition'] = f"attachment; filename*=UTF-8''{urllib.parse.quote(fname)}"
    return response


@login_required
def download_harakteristika(request, doc_id):
    from .docx_generator import generate_harakteristika
    doc    = get_object_or_404(CharacteristicDocument, id=doc_id, user=request.user)
    output = generate_harakteristika(doc)

    fname  = f'Характеристика - {doc.fio or "документ"}.docx'
    response = HttpResponse(
        output,
        content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    )
    response['Content-Disposition'] = f"attachment; filename*=UTF-8''{urllib.parse.quote(fname)}"
    return response

@login_required
def edit_characteristic_document(request, doc_id):
    doc = get_object_or_404(CharacteristicDocument, id=doc_id, user=request.user)

    if request.method == 'POST':
        doc.fio              = request.POST.get('fio', '')
        doc.library          = request.POST.get('library', '')
        doc.work_start       = request.POST.get('work_start') or None
        doc.work_end         = request.POST.get('work_end') or None
        doc.work_days_count  = request.POST.get('work_days_count') or None
        doc.missed_days      = request.POST.get('missed_days') or None
        doc.missed_unexcused = request.POST.get('missed_unexcused') or None
        doc.speciality       = request.POST.get('speciality', '')
        doc.work_quality     = request.POST.get('work_quality', '')
        doc.supervisor       = request.POST.get('supervisor', '')
        doc.save()
        messages.success(request, 'Характеристика обновлена!')
        return redirect('/profile/#my-docs')

    return render(request, 'edit_characteristic_document.html', {'doc': doc})

@login_required
def delete_characteristic_document(request, doc_id):
    doc = get_object_or_404(CharacteristicDocument, id=doc_id, user=request.user)
    doc.delete()
    messages.success(request, 'Характеристика удалена!')
    return redirect('/profile/#my-docs')

def logout_view(request):
    logout(request)
    return redirect('/login/')
