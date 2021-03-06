from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView, UpdateView
from nesting.forms import Identity_Form, Symptom_Form
from nesting.models import Identity_unique, Symptom_relation




class Identity_view(TemplateView):

    template_name = 'nesting/nesting.html'

    def get(self, request):


        form = Identity_Form()

        Identities = Identity_unique.objects.filter(user = request.user)

        var = {'form': form, 'Identities': Identities}

        return render(request, self.template_name, var)

    def post(self, request):



        form  = Identity_Form(request.POST)

        content = None

        if form.is_valid():

            NIS = form.save(commit = False)
            NIS.user = request.user
            NIS.save()


            content = form.cleaned_data['NIS']

            form = Identity_Form()


            return redirect('nesting:nesting')

        var = {'form': form, 'content': content}

        return render(request,self.template_name, var)





class Identity_nest_list_view(TemplateView):



    model = Identity_unique

    template_name = 'nesting/Identity_nest.html'


    def get(self, request):

        form = Identity_Form()

        Identities = Identity_unique.objects.filter(user = request.user).order_by('-Timestamp')
        var = {'form':form, 'Identities': Identities}
        return render(request, self.template_name, var)





class Symptoms_document_view(TemplateView):

    model = Symptom_relation

    template_name = 'nesting/Symptoms_list.html'

    def get(self, request, pk):

        form = Symptom_Form()


        Symptoms_desc = Symptom_relation.objects.all()
        #Symptoms_desc = Identity_unique.objects.get(pk = pk).Symptom_relation_set


        var = {'form':form, 'Symptoms_desc':Symptoms_desc, 'pk':pk}


        return render(request, self.template_name, var)



    def post(self, request, pk):

        form = Symptom_Form(request.POST )

        Symptom_content = None

        if form.is_valid():

            Symptom_description = form.save(commit = False)
            Symptom_description.user = request.user

            Symptom_content = form.cleaned_data['symptom_description']



            Symptom_description.save()
            Identity_set_unique = Identity_unique.objects.get(pk=pk)

            Symptom_description.Unique_Identity.add(Identity_set_unique)
            Symptom_description.save()



            form = Symptom_Form()


            redirect('nesting:nesting')

        var = {'form': form, 'Symptom_content': Symptom_content, 'pk':pk}

        return render(request, self.template_name, var)




class Medical_History_nest_view(TemplateView):


    model = Symptom_relation

    template_name = 'nesting/Medical_History_nest.html'

    def get(self, request, pk):

        form = Symptom_Form()

        Symptoms_desc = Symptom_relation.objects.all()
        Symptoms_desc = Identity_unique.objects.get(pk=pk).Symptom.all()

        var = {'form':form, 'Symptoms_desc':Symptoms_desc}

        return render(request, self.template_name, var)


class Identity_unique_Update(UpdateView):

    model = Identity_unique

    fields = [ 'first_Name', 'last_Name', 'location', 'date_of_birth', 'contact',]

    def get_success_url(self):
        success_url = reverse('nesting:Identity_nest_list', kwargs={'pk': self.object.pk})
