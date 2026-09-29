# Git & GitHub Quickstart Guide for Beginners

> **Audience:** Anyone new to version control. No prior programming or terminal experience required.  
> **Goal:** Create your homework repository, understand the expected folder structure, and learn how to upload your assignments.

---

## 1. What Are Git and GitHub? (In 30 Seconds)

* **Git** is a version-tracking tool on your computer. It creates saved checkpoints ("commits") of your files so you can track your progress, see what changed, or recover previous versions.
* **GitHub** is a secure cloud platform. It acts as an online storage hub where your repositories live, making it easy to submit homework, share work, and receive feedback from instructors.

---

## 2. Step 1: Create Your Free GitHub Account

If you do not already have a GitHub account:
1. Open **[github.com/signup](https://github.com/signup)** in your browser.
2. Enter your email address and create a secure password.
3. Choose a professional username (e.g., `ihar-rubanovich-epam` or `first-last`).
4. Complete the quick verification puzzle and confirm the code sent to your email.

---

## 3. Step 2: Create Your Homework Repository (`genai-homeworks`)

Once you are logged into GitHub:
1. In the top-right corner of the page, click the **`+`** icon and select **New repository**.
2. Fill in the repository details:
   * **Repository name:** `genai-homeworks`
   * **Description:** `GenAI Basics course homework and engineering memos`
   * **Visibility:** Choose **Private** (recommended) or **Public**.
   * **Initialize repository:** Check the box **"Add a README file"** *(Important: this initializes the repository with a main branch immediately, so you can start creating files right in your browser)*.
3. Click the green **Create repository** button.

---

## 4. Step 3: Expected Course Folder Structure

Throughout this course, you will submit assignments into individual lesson folders within this single repository. 

Here is what your repository structure will look like over time:

```text
genai-homeworks/
├── README.md               <-- Main repository overview (course table of contents)
├── L01/
│   └── README.md           <-- Lesson 01: AI Use-Case Memo
├── L02/
│   └── README.md           <-- Lesson 02: Prompt Engineering & Schemas
├── L03/
│   └── README.md           <-- Lesson 03: RAG Architecture
└── ...
```

### The GitHub "Folder Trick" (Crucial for Beginners)
> [!NOTE]
> Git does **not** track empty folders, so there is no separate "Create Folder" button in GitHub's web interface.  
> To create a folder on GitHub:
> 1. Click **Add file** ➔ **Create new file**.
> 2. In the filename input box, type the folder name followed by a forward slash `/`, then the file name:  
>    `L01/README.md`
> 3. As soon as you type the `/`, GitHub automatically turns `L01` into a folder!

---

## 5. Step 4: Three Ways to Submit Your Work (Choose One)

You do **not** have to use a black terminal screen if you are not comfortable with command lines. Choose the path that fits you best:

### Option A: 100% In the Browser (Easiest — No Tools Installed)
1. Go to your `genai-homeworks` repository on [github.com](https://github.com).
2. Click **Add file** (near the top right of the file list) ➔ **Create new file**.
3. In the filename box, type: `L01/README.md`.
4. In the large text area below, type or paste your completed assignment (e.g., your AI Use-Case Memo).
5. Scroll down to the **Commit changes** box at the bottom:
   * Leave the default message (or enter: `feat(L01): add use-case memo`).
   * Keep **"Commit directly to the main branch"** selected.
6. Click the green **Commit changes** button. Your folder and homework file are now saved and visible on GitHub!

---

### Option B: The Modern AI Agent Way (Google Antigravity / Cursor)
If you prefer working locally inside an AI-enabled editor like **Google Antigravity** or **Cursor**:
1. Open your local `genai-homeworks` folder in the editor.
2. Create the file `L01/README.md` and write your assignment.
3. Open the AI Agent panel by pressing **`Ctrl + L`** (Windows) or **`Cmd + L`** (Mac).
4. Type a natural prompt in plain language:
   > *"Commit my L01 homework with a descriptive commit message and push it to my GitHub repository."*
5. The AI agent will inspect your changes, draft the exact terminal commands, and present an **Approve** button.
6. Click **Approve**. The AI executes the Git workflow for you.

---

### Option C: The Classic Command Line (For Learning Git CLI)
If you want to practice standard developer command-line workflows:
1. **Download & install Git:** [git-scm.com/downloads](https://git-scm.com/downloads) (accept all installer defaults).
2. **Set your author identity (one-time setup):**
   Open PowerShell or Terminal and run:
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "your-github-email@example.com"
   ```
3. **Clone your repository locally:**
   ```bash
   git clone https://github.com/your-username/genai-homeworks.git
   cd genai-homeworks
   ```
4. **Create the folder and file:**
   Create an `L01` folder and place `README.md` inside it.
5. **Stage, commit, and push:**
   ```bash
   git add L01/README.md
   git commit -m "feat(L01): add use-case memo"
   git push origin main
   ```

---

## 6. Step 5: Invite Your Instructor for Review

To allow your instructor to view and grade your private repository:
1. Open your `genai-homeworks` repository on [github.com](https://github.com).
2. Click the **Settings** tab (the gear icon on the top navigation bar).
3. In the left sidebar, click **Collaborators** (under the "Access" section).
4. Click the green **Add people** button.
5. In the search box, enter the instructor's email:
   ```text
   ihar_rubanovich@epam.com
   ```
6. Click **Add ihar_rubanovich@epam.com to this repository**.
7. Copy your repository URL (e.g., `https://github.com/your-username/genai-homeworks`) and submit it in the course portal.

---

## 7. Recommended Quick Reads (Zero Fluff)

For a quick 5-to-10 minute conceptual overview:
* **[Git — The Simple Guide](https://rogerdudler.github.io/git-guide/)**  
  A clean, single-page visual guide explaining commits, remotes, and branches in plain terms.
* **[GitHub Skills](https://skills.github.com/)**  
  Free, 10-minute interactive tutorials running directly inside GitHub.
* **[Learn Git Branching](https://learngitbranching.js.org/)**  
  A visual interactive playground for visualizing Git history.
