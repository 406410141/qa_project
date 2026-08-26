import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
    // Test location
    testDir: './tests',

    // Run test files in parallel
    fullyParallel: true,

    // Prevent test.only from being committed to CI
    forbidOnly: !!process.env.CI,

    // Retry failed tests only on CI
    retries: process.env.CI ? 2 : 0,

    // Use one worker on CI to reduce environment-related instability
    workers: process.env.CI ? 1 : undefined,

    // Test timeout
    timeout: 30 * 1000,

    // Reporter
    reporter: [
        ['list'],

        [
            'html',
            {
                outputFolder: 'playwright-report',
                open: 'never',
            },
        ],

        [
            'allure-playwright',
            {
                outputFolder: 'allure-results', 
            },
        ],
    ],

    // Shared settings
    use: {
        // SauceDemo base URL
        baseURL: 'https://www.saucedemo.com',

        // Collect trace when test fails
        trace: 'retain-on-failure',

        // Take screenshot when test fails
        screenshot: 'only-on-failure',

        // Do not record video for now
        video: 'off',

        // Run browser in headless mode by default
        headless: true,
    },

    // Test results / artifacts
    outputDir: 'test-results',

    // Browser projects
    projects: [
        {
            name: 'chromium',
            use: {
                ...devices['Desktop Chrome'],
            },
        },

        {
            name: 'firefox',
            use: {
                ...devices['Desktop Firefox'],
            },
        },

      // WebKit 暫時不作為預設測試
    // {
    //     name: 'webkit',
    //     use: { ...devices['Desktop Safari'] },
    // },
    ],
});