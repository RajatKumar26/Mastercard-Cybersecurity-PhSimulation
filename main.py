import re

def generate_professional_phishing_email(employee_name, target_link):
    subject = "URGENT: Mastercard Security Update - Immediate Action Required"
    
    masked_link = f"[Mastercard IT Security Portal]({target_link})"
    
    body = f"""
Dear {employee_name},

As part of Mastercard's quarterly security infrastructure upgrade, all global employees are required to verify their security credentials within the next 24 hours. 

Failure to complete this verification will result in the temporary suspension of your corporate network access.

Please click the official link below to secure your identity:
👉 {masked_link}

Thank you for your cooperation in keeping Mastercard secure.

Regards,
Mastercard IT Security Team
Corporate Identity Management
    """
    return subject, body
if __name__ == "__main__":
    sample_name = "John Doe"
    simulation_link = "https://en.wikipedia.org/wiki/Phishing" # Fake link provided by Forage

    email_subject, email_body = generate_professional_phishing_email(sample_name, simulation_link)

    print(f"Subject: {email_subject}")
    print(email_body)