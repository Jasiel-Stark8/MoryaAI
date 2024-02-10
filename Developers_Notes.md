# Developer Notes for MoryaAI Team

## Project Overview

MoryaAI is an AI-powered content creation tool designed to streamline the writing process, enhance content quality, and maximize audience engagement. The application uses Vue.js/PrimeVue for the frontend and Flask for the backend.

## Core Features

Our focus during the initial development phase will be on the following core features:

1. **Adaptive Content Style**: Tailors writing style to audience preferences and platform norms.
2. **Semantic Content Enhancement**: Enriches content with relevant data and multimedia.
3. **Collaborative Editing with AI Assistance**: Facilitates seamless collaboration with AI-driven edits.
4. **Cross-Platform Publishing**: Enables one-click publishing across multiple platforms.
5. **Automated SEO Optimization**: Integrates SEO best practices to enhance content discoverability.
6. **Voice-to-Text Article Drafting**: Converts voice dictation into structured, formatted articles.

## Technology Stack

- **Frontend**: Vue.js/PrimeVue
- **Backend**: Flask
- **AI Models**: OpenAI's GPT-4 | Llama | Mixtral | Gemini
- **CI/CD**: Jenkins | GitHub Actions
- **Server Hosting**: AWS EC2 | Google Cloud Compute Engine
- **Database**: PostgreSQL | MongoDB
- **Logging and Monitoring**: ELK Stack (Elasticsearch, Logstash, Kibana) | Google Stackdriver
- **Security**: Bcrypt for password hashing | 2FA for user authentication | SSL for secure data transmission
- **Scale Performance & Optimization**: Load balancing with Nginx | Caching with Redis | CDN with Cloudflare

## Development Guidelines

### Frontend Guidelines

- Follow the [Vue.js style guide](https://vuejs.org/v2/style-guide/) and [PrimeVue guidelines](https://primevue.org/) for code consistency.
- Write unit tests for all new features and bug fixes.
- Use clear, descriptive commit messages.

### Backend Guidelines

- Follow the [Flask style guide](https://flask.palletsprojects.com/en/3.0.x/styleguide/) for code consistency.
- Write unit tests for all new features and bug fixes.
- Use clear, descriptive commit messages.

### Collaborative Methods and Practices

- Submit pull requests for all changes, and ensure they are reviewed by at least one other team member before merging.
- Regularly sync your local development branch with the main branch.
- Use feature branches for developing new features or fixing bugs.
- Use descriptive names for your branches (e.g., `feature/user-authentication`, `bugfix/header-styling`).

## Setup Instructions

1. Clone the repository to your local machine.
2. Install the required dependencies.
3. Set up your API keys for Medium, HashNode, LinkedIn.

## Useful Commands

- `npm run serve`: Starts the development server for the Vue.js frontend.
- `flask run`: Starts the Flask backend server.

## Troubleshooting

If you encounter any issues during development, please refer to the respective documentation for Vue.js, PrimeVue, and Flask. If the issue persists, reach out to the team for assistance.

## Contact

For any queries or assistance, please reach out to the project lead or any of the team members.
