import http from 'k6/http';
import { check, sleep } from 'k6';
import { htmlReport } from "https://raw.githubusercontent.com/benc-uk/k6-reporter/main/dist/bundle.js";

export const options = {

    stages: [
        { duration: '3s', target: 1200 },  
        { duration: '10s', target: 1200 }, 
        { duration: '3s', target: 0 }      
    ],
    thresholds: {
        
        http_req_duration: ['p(99)<1000'], 
        http_req_failed: ['rate<0.20']    
    }
};


export default function () {
    const url = 'https://restful-booker.herokuapp.com/booking';
    
    const payload = {
        "firstname": "K6_Performance",
        "lastname": "Test",
        "totalprice": 500,
        "depositpaid": true,
        "bookingdates": {
            "checkin": "2026-07-01",
            "checkout": "2026-07-02"
        },
        "additionalneeds": "Late check-in"
    };
    
    const headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    };
    
    const res = http.post(url, JSON.stringify(payload), { headers: headers });
    
    
    if (res.status >= 500) {
        console.log(`Server error! Status: ${res.status}, Response: ${res.body}`);
    }
    
    if (res.status === 200) {
        try {
            const resBody = res.json();
            if (resBody.hasOwnProperty('bookingid')) {
                console.log(`成功建立訂單！ID: ${resBody.bookingid}`);
            }
        } catch (e) {
            console.log(`status == 200 but body is not valid JSON: ${res.body}`);
        }
    }
    
    check(res, {
        'is status 200': (r) => r.status === 200,
        'has bookingid': (r) => {
        try {
            return r.json().hasOwnProperty('bookingid');
        } catch (e) {
            return false;
        }
    }
    });
    
    sleep(1);   
}

export function handleSummary(data) {
    return {
        "report_data/spike_test_summary.html": htmlReport(data), 
        "report_data/spike_test_summary.json": JSON.stringify(data),

    };
}


//k6 run --summary-export=report.json script.js

    


    

    

