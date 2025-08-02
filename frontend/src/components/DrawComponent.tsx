import React, { useRef, useState, useEffect } from 'react';

const CANVAS_SIZE = 280;
const TARGET_SIZE = 28;

interface DrawingCanvasProps {
handlePredict: (imageData: number[]) => void;
}

const DrawingCanvas: React.FC<DrawingCanvasProps> = ({ handlePredict }) => {

    const canvasRef = useRef<HTMLCanvasElement>(null);
    const [drawing, setDrawing] = useState(false);

    useEffect(() => {
        clearCanvas();
    }, []);

    const startDrawing = (e: React.MouseEvent) => {
        const ctx = canvasRef.current!.getContext('2d')!;
        ctx.lineWidth = 20;
        ctx.lineCap = 'round';
        ctx.lineJoin = 'round';
        ctx.strokeStyle = 'black';
        ctx.beginPath();
        ctx.moveTo(e.nativeEvent.offsetX, e.nativeEvent.offsetY);
        setDrawing(true);
    };

    // Continue
    const draw = (e: React.MouseEvent) => {
        if (!drawing) return;
        const ctx = canvasRef.current!.getContext('2d')!;
        ctx.lineTo(e.nativeEvent.offsetX, e.nativeEvent.offsetY);
        ctx.stroke();
    };

    const stopDrawing = () => {
        setDrawing(false);
    };

    const clearCanvas = () => {
        const ctx = canvasRef.current!.getContext('2d')!;
        ctx.fillStyle = 'white';
        ctx.fillRect(0, 0, CANVAS_SIZE, CANVAS_SIZE);
    };

    // Convert to 1D array
    const getImageData = (): number[] => {
        const srcCanvas = canvasRef.current!;

        const tmpCanvas = document.createElement('canvas');
        tmpCanvas.width = TARGET_SIZE;
        tmpCanvas.height = TARGET_SIZE;
        const tmpCtx = tmpCanvas.getContext('2d')!;

        // draw it after scaling
        tmpCtx.imageSmoothingEnabled = true;
        tmpCtx.imageSmoothingQuality = 'high';
        tmpCtx.drawImage(srcCanvas, 0, 0, TARGET_SIZE, TARGET_SIZE);

        const imageData = tmpCtx.getImageData(
            0,
            0,
            TARGET_SIZE,
            TARGET_SIZE
        ).data;

        const pixels: number[] = [];
        for (let i = 0; i < imageData.length; i += 4) {
            const [r, g, b] = [
                imageData[i],
                imageData[i + 1],
                imageData[i + 2],
            ];

            const gray = (r + g + b) / 3;

            const normalized = (255 - gray) / 255;
            pixels.push(normalized);
        }

        return pixels;
    };

    const handleExport = () => {
        const pixels = getImageData();
        handlePredict(pixels);
    };

    return (
        <div style={{ textAlign: 'center' }}>
            <h3>Draw a digit</h3>
            <canvas
                className="drawing-canvas"
                ref={canvasRef}
                width={CANVAS_SIZE}
                height={CANVAS_SIZE}
                style={{ border: '1px solid black', backgroundColor: 'white' }}
                onMouseDown={startDrawing}
                onMouseMove={draw}
                onMouseUp={stopDrawing}
                onMouseLeave={stopDrawing}
            />
            <div className="drawing-controls">
                <button className="clear-button" onClick={clearCanvas}>
                    Clear
                </button>
                <button className="predict-button" onClick={handleExport}>
                    predict
                </button>
            </div>
        </div>
    );
};

export default DrawingCanvas;
