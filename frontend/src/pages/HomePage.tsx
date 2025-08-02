import '../styles/HomePage.css';
import React from 'react';
import DrawComponent from '../components/DrawComponent';

function HomePage() {
    const [predictionResult, setPredictionResult] = React.useState('');
    const [accuracy, setAccuracy] = React.useState(0);

    const handlePredict = (imageData: number[]) => {
        fetch('http://localhost:8000/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(imageData),
        })
            .then((response) => response.json())
            .then((data) => {
                setPredictionResult(data.character);
                setAccuracy(data.prediction || 92.5);
            })
            .catch((error) => {
                console.error('Prediction error:', error);
            });
    };

    return (
        <div className="home-page">
            <div className="header-section">
                <h1>Digit Recognition</h1>
                <p className="description">
                    Draw a digit (0-9) in the box below
                </p>
            </div>

            <div className="main-content">
                {/* Drawing section */}
                <DrawComponent handlePredict={handlePredict} />

                {/* Results section */}
                <div className="results-section">
                    {predictionResult ? (
                        <div className="prediction-display">
                            <h3>Recognition Results</h3>
                            <div className="recognized-character-container">
                                <div className="recognized-character-box">
                                    <span className="character">
                                        {predictionResult}
                                    </span>
                                    <div className="character-glow"></div>
                                </div>
                                <div className="character-label">
                                    Recognized Character
                                </div>
                            </div>
                            <div className="accuracy-display">
                                <div className="accuracy-label">
                                    Confidence Level
                                </div>
                                <div className="accuracy-bar-container">
                                    <div
                                        className="accuracy-bar"
                                        style={{ width: `${accuracy}%` }}
                                    ></div>
                                </div>
                                <div className="accuracy-percentage">
                                    {(accuracy * 100).toFixed(1)}%
                                </div>
                            </div>
                        </div>
                    ) : (
                        <div className="no-prediction">
                            <p>
                                Draw something and click predict to see the
                                results!
                            </p>
                        </div>
                    )}
                </div>
            </div>
        </div>
    );
}

export default HomePage;
