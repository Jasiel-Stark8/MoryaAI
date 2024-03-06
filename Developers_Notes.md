# Developer Notes for MoryaAI Team

## Project Overview

MoryaAI is an AI-powered content creation tool designed to streamline the writing process, enhance content quality, and maximize audience engagement. \
A one-click generate and post AI Application! \
The application uses Vue.js/PrimeVue for the frontend and Flask for the backend. \

#### NOTE:
As discussed in our team meeting, we are developing a foundational model for our software; starting with 83M(Rolling out on Tuesday); 7B; then 13B models. \
This way we have full control, and we may later decide to monetize it. \
For any queries or model bug reports contact Jason :)


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
    - Foundational Model is in development | We will scrap the above models this week
- **CI/CD**: Jenkins | GitHub Actions
- **Server Hosting**: AWS EC2 | Google Cloud Compute Engine
- **Database**: MongoDB
- **Payment Platform**: Stripe
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

### Backend Structure

```
.
├── Developers_Notes.md
├── LICENSE
├── README.md
├── client
│   ├── file
│   ├── public
│   │   ├── README.md
│   │   ├── env.d.ts
│   │   ├── index.html
│   │   ├── package-lock.json
│   │   ├── package.json
│   │   ├── postcss.config.js
│   │   ├── src
│   │   │   ├── App.vue
│   │   │   ├── assets
│   │   │   │   ├── base.css
│   │   │   │   ├── logo.svg
│   │   │   │   └── main.css
│   │   │   ├── components
│   │   │   │   ├── DashboardPage.vue
│   │   │   │   ├── GenerationPage.vue
│   │   │   │   ├── ProfilePage.vue
│   │   │   │   ├── SignIn.vue
│   │   │   │   ├── SignUp.vue
│   │   │   │   ├── __tests__
│   │   │   │   │   └── HelloWorld.spec.ts
│   │   │   │   └── icons
│   │   │   │       ├── IconCommunity.vue
│   │   │   │       ├── IconDocumentation.vue
│   │   │   │       ├── IconEcosystem.vue
│   │   │   │       ├── IconSupport.vue
│   │   │   │       └── IconTooling.vue
│   │   │   ├── index.css
│   │   │   ├── main.ts
│   │   │   ├── router
│   │   │   │   └── index.ts
│   │   │   ├── stores
│   │   │   │   └── counter.ts
│   │   │   ├── test
│   │   │   └── views
│   │   │       └── SideBar.vue
│   │   ├── tailwind.config.js
│   │   ├── tsconfig.app.json
│   │   ├── tsconfig.json
│   │   ├── tsconfig.node.json
│   │   ├── tsconfig.vitest.json
│   │   ├── vite.config.ts
│   │   └── vitest.config.ts
│   └── tes
└── server
    ├── app
    │   ├── __init__.py
    │   ├── api
    │   │   ├── __init__.py
    │   │   └── v1
    │   │       ├── core
    │   │       │   ├── __init__.py
    │   │       │   ├── auth.py
    │   │       │   ├── generate.py
    │   │       │   ├── settings.py
    │   │       │   ├── subscribe.py
    │   │       │   └── view_articles.py
    │   │       ├── llms
    │   │       │   ├── GPT-2-conversation_dataset.json
    │   │       │   ├── __init__.py
    │   │       │   ├── distil.py
    │   │       │   ├── distilgpt2
    │   │       │   │   ├── 64.tflite
    │   │       │   │   ├── README.md
    │   │       │   │   ├── config.json
    │   │       │   │   ├── coreml
    │   │       │   │   │   └── text-generation
    │   │       │   │   │       └── float32_model.mlpackage
    │   │       │   │   │           ├── Data
    │   │       │   │   │           │   └── com.apple.CoreML
    │   │       │   │   │           │       ├── model.mlmodel
    │   │       │   │   │           │       └── weights
    │   │       │   │   │           │           └── weight.bin
    │   │       │   │   │           └── Manifest.json
    │   │       │   │   ├── coreml_model.mlmodel
    │   │       │   │   ├── flax_model.msgpack
    │   │       │   │   ├── generation_config.json
    │   │       │   │   ├── generation_config_for_text_generation.json
    │   │       │   │   ├── merges.txt
    │   │       │   │   ├── model.safetensors
    │   │       │   │   ├── pytorch_model.bin
    │   │       │   │   ├── rust_model.ot
    │   │       │   │   ├── tf_model.h5
    │   │       │   │   ├── tokenizer.json
    │   │       │   │   ├── tokenizer_config.json
    │   │       │   │   └── vocab.json
    │   │       │   ├── finetune.py
    │   │       │   ├── pat
    │   │       │   ├── post.py
    │   │       │   └── train.py
    │   │       └── routes
    │   │           └── __init__.py
    │   ├── database.py
    │   └── models
    │       ├── __init__.py
    │       ├── articles.py
    │       ├── platforms.py
    │       ├── published_content.py
    │       ├── users.py
    │       └── voice_drafts.py
    ├── app.py
    ├── requirements.txt
    └── tests
        ├── __init__.py
        └── test_auth.py

27 directories, 84 files
```

### Database & Storage

1. User Information
   - Username
   - Email
   - Hashed Password
   - Profile Picture
   - Subscription Status
   - Authentication Provider (Google, LinkedIn)

2. Article Information
   - Title
   - Content
   - Status (Draft or Published)
   - Auto-save Timestamps
   - Author (reference to User)

3. Platform Information
   - Platform Name (Medium, Hashnode, LinkedIn)
   - API Keys or other necessary details for each platform

4. Subscription Plan Information
   - Plan Name
   - Plan Features
   - Plan Price

5. Payment Information
   - User (reference to User)
   - Payment Method
   - Transaction ID
   - Date of Transaction
   - Subscription Purchased (reference to Subscription Plan)

6. Saved Content Information
   - User (reference to User)
   - Content (reference to Article)
   - Date Saved

7. Published Content Information
   - User (reference to User)
   - Content (reference to Article)
   - Platform Published On
   - Link to Published Content

8. Voice Draft Information
   - User (reference to User)
   - Content
   - Date Created

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

---
# User Visuals
Structured application outline:

1. **Join Waitlist/Signup/Login**: Users start by joining a waitlist, signing up for an account, or logging in if they already have an account.

2. **Dashboard**: After logging in, users are taken to their dashboard. The dashboard has the following sections:

    - **Content Generation**: This section provides a quick link to the content generation page. It might also display the most recent content generated by the user, or some statistics about their content generation (like the total number of articles generated, the total word count, etc.).

    - **Saved Content**: This section displays the content that the user has saved for later. Users can click on a piece of content to view it, edit it, export it, or publish it.

    - **Published Content**: This section displays the content that the user has published. It might include links to the published content on the various platforms.

    - **Account Settings**: This section provides a link to the profile settings page, where users can manage their account and personal details.

    - **Upgrade**: This section provides a link to the upgrade page, where users can upgrade their account for additional features.

3. **Content Generation Page**:
    - Left:
        - Title
        - Keywords
        - Length (drop-down)
        - Generate
        - Voice to text

    - Right:
        - Generated content

    - Page Actions (Determine postion on page):
        - Edit
        - Save
        - Copy
        - Export:
            - PDF
            - DOCX
            - MD
            - TXT
        - Publish:
            - Medium
            - Hashnode
            - LinkedIn

4. **Profile Settings Page**: On this page, users can manage their account and personal details:
    - Changing password
    - updating email address
    - Manage subscription
    - Update profile picture
    - Theme

5. **Upgrade Page**: On this page, users can upgrade their account for additional features:
    - Choose a subscription plan
    - Enter/update payment details

Dashboard layout description:

- The dashboard is divided into several sections, each represented by a card or panel. Each section has a title and a brief description or preview of its content.

- The **Content Generation** section is at the top. It includes a "Generate New Content" button and a preview of the most recent content generated by the user.

- Below that is the **Saved Content** section, which displays a list of the user's saved content. Each item in the list includes the title of the content, a brief excerpt, and buttons for viewing, editing, exporting, and publishing the content.

- The **Published Content** section is similar to the Saved Content section, but it displays the user's published content instead. Each item in the list includes the title of the content, the platform it was published on, and a link to the published content.

- The **Account Settings** and **Upgrade** sections are at the bottom. Each section includes a button that takes the user to the corresponding page.

- The dashboard also includes a sidebar or navigation menu with links to the main pages of the application (Dashboard, Content Generation, Profile Settings, Upgrade). The menu will also include links to help resources, user guides, and customer support.

---

## Contact

For any queries or assistance, please reach out to the project lead <Jason> or any of the team members.

&copy; Morya AI Team 2024
<Jason> & <Angela>
This product is licensed under <GNU GENERAL PUBLIC LICENSE 3.0>. \
This is strictly to only be seen by Mentor of ALX | Afterward this repo will be closed and restructured accordingly as seen fit by the developers and owners fo this project. \
Note: This project will continue to be worked on and be ready for an April Beta release.
