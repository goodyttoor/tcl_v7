from fastapi import FastAPI

from .core import disease, guardian, history, hospital, patient, procedure, reference, user
from .extension.history import appointment_opd, appointment_or, chief_complaint, conference_ent_plastic, \
    conference_ortho_plastic, conference_summary_treatment, gallery_opd, gallery_or, home_visit, problem, refer, \
    speech, travel_reimburse, treatment, vpi
# from .extension.aorsormor import follow_appointment, follow_operation, search
# from .extension import audit, dashboard, export

app = FastAPI()

# Core modules
app.include_router(disease.router)
app.include_router(guardian.router)
app.include_router(history.router)
app.include_router(hospital.router)
app.include_router(patient.router)
app.include_router(procedure.router)
app.include_router(reference.router)
app.include_router(user.router)

# Extension modules (history)
app.include_router(appointment_opd.router)
app.include_router(appointment_or.router)
app.include_router(chief_complaint.router)
app.include_router(conference_ent_plastic.router)
app.include_router(conference_ortho_plastic.router)
app.include_router(conference_summary_treatment.router)
app.include_router(gallery_opd.router)
app.include_router(gallery_or.router)
app.include_router(home_visit.router)
app.include_router(problem.router)
app.include_router(refer.router)
app.include_router(speech.router)
app.include_router(travel_reimburse.router)
app.include_router(treatment.router)
app.include_router(vpi.router)

# # Extension modules (aorsormor)
# app.include_router(follow_appointment.router)
# app.include_router(follow_operation.router)
# app.include_router(search.router)
#
# # Extension modules
# app.include_router(audit.router)
# app.include_router(dashboard.router)
# app.include_router(export.router)
