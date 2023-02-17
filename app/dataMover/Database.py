from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import declarative_base, relationship
from flask_sqlalchemy import SQLAlchemy

class ProcessDb(Base.Model):

    __tablename__ = 'process'

    processId = Column(Integer, primary_key=True)
    globalId = Column(String(40), nullable=False)
    pid = Column(Integer, nullable=True)
    scheduledFor = Column(DateTime, nullable=True)
    start = Column(DateTime, nullable=True)
    stop = Column(DateTime, nullable=True)
    forceful = Column(Boolean, nullable=True)
    processStatus = Column(Integer, nullable=False)

    folder = relationship('FolderDb', backref='folder')
    __table_args__ = (UniqueConstraint('pid', 'stop', name='pid_stop_constaint'),)

    def __repr__(self):
        return f"Book(                          \
            globalId={self.globalId!r},         \
            pid={self.pid!r},                   \
            start={self.start!r},               \
            stop={self.stop!r}                  \
            scheduledFor={self.scheduledFor!r}  \
            processStatus={self.processStatus!r}\
            forcefull={self.forceful!r})"
    
    def serialize(self):
        return {
            'globalId' : self.globalId,
            'pid' : self.pid,
            'start' : self.start,
            'stop' : self.stop,
            'scheduledFor' : self.scheduledFor,
            'processStatus' : self.processStatus,
            'forcefull' : self.forceful
        }

class FolderDb(Base.Model):
    
    __tablename__ = 'folder'

    folderId = Column(Integer, primary_key=True)
    processId = Column(Integer, ForeignKey('process.processId'), nullable=False)
    folderName = Column(String, nullable=False)
    folderPath = Column(String, nullable=False)

    def __repr__(self):
        return f"Book(                     \
            processId={self.processId!r},  \
            folderName={self.folderName!r},\
            folderPath={self.folderPath!r}"
