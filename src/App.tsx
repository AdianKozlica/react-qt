import React from "react"

declare global {
    interface Window {
        qtObject: {
            sendSignal: (arg) => void;
        };
    }
}

export default function App() {
    return (
        <div>
            <button onClick={() => window.qtObject.sendSignal('Hello')}>Send signal</button>
            <h1>Hello World</h1>
        </div>
    )
}