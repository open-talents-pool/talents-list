# Open Talents Pool

Welcome to the Open Talents Pool! This repository is designed to be an open and transparent platform where IT professionals, especially programmers, can register themselves. It serves as a public talent pool where companies and individuals can search for potential candidates based on their skills, location, and other criteria.

## How It Works

1. **Registration**: IT professionals can register by triggering a GitHub Action that requires some manual inputs.
2. **Information Storage**: The provided information is saved in a JSON file within this repository, making it publicly available.
3. **Searchable Database**: Companies and recruiters can easily search through the information via a web UI to find potential candidates.

## Registration Process

To register yourself in the Open Talents Pool, follow these steps:

1. **Trigger the GitHub Action** named [Register In Open Talents Pool](https://github.com/open-talents-pool/talents-list/actions/workflows/register-in-open-talents-pool.yml) in this repository.
2. **Provide the necessary inputs** as described below.
3. **Commit and push** the changes.

### GitHub Action: Register In Open Talents Pool

The GitHub Action requires the following inputs:

- **Name**: Your full name (required)
- **Contact Link**: A link to your LinkedIn profile, personal website, or any link to your CV (required)
- **Email Address**: Your email address (optional, but recommended)
- **Primary Role Title**: Your main job title (required)
- **Country of Residence**: The country you are living in (required)
- **City of Residence**: The city you are living in (optional)
- **Technical Skills**: Your main technical skills (comma-separated) (required)
- **Communication Languages**: Languages you can communicate in (comma-separated) (required)
- **Willing to Relocate**: Whether you are willing to relocate (true/false) (required)
- **Willing for Remote Work**: Whether you are willing to work remotely (true/false) (required)

### Example

To trigger the GitHub Action, go to the "Actions" tab in this repository, select the `Register In Open Talents Pool` workflow, and click "Run workflow". Fill in the required inputs as prompted.

## Privacy Notice

- **Public Information**: The information you provide will be publicly available in this repository. Please do not include sensitive or private information.
- **Optional Email**: Providing your email address has several benefits:
  - **Profile Maintenance**: You will receive an email each month with a link to extend the active status of your profile. If you do not extend the profile within one month, it will be assumed that you no longer wish to be open to work, and your profile will be deleted.
  - **Job Notifications**: Companies and individuals can inform you about potential job opportunities through the Open Talents Pool web UI, and you will receive these notifications via email.

## Searching the Talent Pool

The information is stored in JSON format and is made searchable via a web UI. You can search for candidates based on various criteria such as technical skills, location, willingness to relocate, and more.

## Contributing

We welcome contributions to improve this repository. If you have any ideas or suggestions, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

By registering, you agree to have your information publicly available in this repository. This is an open initiative to help connect IT professionals with potential job opportunities.

Thank you for being a part of the Open Talents Pool!
