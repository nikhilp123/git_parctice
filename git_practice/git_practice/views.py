# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
import json

from random import randint
from django.http import HttpRequest, HttpResponse, JsonResponse, HttpResponseRedirect
from .helper_functions import create_patient_function,create_enquiry_function,edit_patient_function,get_all_patients_function,get_all_enquires_function,convert_enquiry_to_patient_function,search_patient_function,search_enquiry_function,is_doctor,is_front_desk,create_case_function,get_patient_detail_by_id_function,create_questionnaire_function,get_case_questionnaire,create_clinical_findings_function,get_clinical_findings_function,reauthenticate_staff_member_function,get_all_choices_and_id_app_function,get_patient_data_by_id_function,get_autocomplete_suggestions_function,edit_enquiry_function,get_enquiry_detail_by_id_function,get_default_questionnaire_function,edit_clinical_findings_function, get_enquiry_autocomplete_suggestions_function,activate_deactivate_patient_function,get_report_document_function,get_validate_input_of_clinical_findings_function,save_result_of_game_function,save_game_profile_function,get_valuation_of_question_response_function
from .validation import validate_patient_params,validate_create_case,validate_enquiry_params,validate_create_questionnaire,validate_create_clinical_findings,validate_create_appointment
from kanohi_web.helper_functions import is_franchisee_admin, is_kanohi_admin
from .appointment_functions import create_appointment_function,get_all_appointments_function,search_appointment_function,edit_appointment_function
from .models import CheckUpLog, GameResult, Patient, GameProfile
# ----------------------------------------------------------------------------------------------------------------------
# Create your views here.
#---------------------------------------------------------------------------------------------------------------

def loginIndex(request):
    return render_to_response('html_templates/loginIndex.html')

def doctorIndex(request):
    return render_to_response('doctorIndex.html')

#-----------------------------------------------------------------------------------------------------------------------------
