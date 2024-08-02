import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';

// Declarations go in index.tsx
declare global {
    interface Window {
        qtObject: {
            sendSignal: (arg) => void;
        };
    }
}

const root = ReactDOM.createRoot(document.getElementById("root") as HTMLElement);
root.render(<App/>)